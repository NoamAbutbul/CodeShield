import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';
import { marked } from 'marked';

/**
 * Activates the extension by registering the security check command.
 * 
 * @param {vscode.ExtensionContext} context - The extension context provided by VS Code.
 */
export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('codeShield.securityCheck', () => {
        const pythonScriptPath = path.join(context.extensionPath, 'main.py');
        const venvPath = path.join(context.extensionPath, 'venv', 'bin', 'python');
        const workspaceFolders = vscode.workspace.workspaceFolders;
        
        if (!workspaceFolders || workspaceFolders.length === 0) {
            vscode.window.showErrorMessage('No workspace folder open.');
            console.log('No workspace folders found.');
            return;
        }

        const workspacePath = workspaceFolders[0].uri.fsPath;
        console.log('Workspace path:', workspacePath);

        const options = {
            cwd: context.extensionPath
        };

        exec(`${venvPath} ${pythonScriptPath} ${workspacePath}`, options, (err, stdout, stderr) => {
            if (err) {
                vscode.window.showErrorMessage(`Error: ${err.message}`);
                console.log(`Error: ${err.message}`);
            } else {
                createWebviewPanel(stdout, context.extensionPath);
            }
        });
    });

    context.subscriptions.push(disposable);
}

/**
 * Deactivates the extension. Currently does nothing.
 */
export function deactivate() {}

/**
 * Creates a webview panel to display the security check results.
 * 
 * @param {string} output - The output from the security check.
 * @param {string} extensionPath - The path to the extension directory.
 */
function createWebviewPanel(output: string, extensionPath: string) {
    const panel = vscode.window.createWebviewPanel(
        'codeShieldOutput', // Identifies the type of the webview. Used internally
        'Security Checking Summary', // Title of the panel displayed to the user
        vscode.ViewColumn.One, // Editor column to show the new webview panel in
        {
            enableScripts: true // Enable scripts in the webview
        }
    );

    // Format the output as plain text, replacing HTML tags
    const formattedOutput = formatOutput(output);
    console.log("Formatted output:", formattedOutput);
    
    // And set its HTML content
    panel.webview.html = renderTemplate(formattedOutput, extensionPath);
}

/**
 * Formats the security check output by removing HTML tags and converting markers to new lines.
 * 
 * @param {string} output - The raw output from the security check.
 * @returns {string} - The formatted output as plain text.
 */
function formatOutput(output: string): string {
    return output
        .replace(/<\/?[^>]+(>|$)/g, '') // Remove all HTML tags
        .replace(/(\*\*|<br>|\n)+/g, '\n') // Convert remaining markers to new lines
        .trim(); // Remove leading and trailing whitespace
}

/**
 * Renders the HTML template with the security check output.
 * 
 * @param {string} output - The formatted security check output.
 * @param {string} extensionPath - The path to the extension directory.
 * @returns {string} - The final HTML content with the output injected.
 */
function renderTemplate(output: string, extensionPath: string): string {
    // Load the HTML template from file
    const templatePath = path.join(extensionPath, 'output_template', 'template.html');
    console.log('Template path:', templatePath);
    const template = readFileToString(templatePath);
    const output_html = convertMarkdownToHtml(output)

    // Replace the placeholder with the actual output
    const renderedHtml = template.replace('{{output}}', output_html.toString());
    console.log('Rendered HTML:', renderedHtml);
    return renderedHtml;
}

/**
 * Reads the content of a file into a string.
 * 
 * @param {string} filePath - The path to the file.
 * @returns {string} - The content of the file.
 * @throws {Error} - Throws an error if the file cannot be read.
 */
function readFileToString(filePath: string): string {
    try {
        console.log('Reading file from path:', filePath);
        const absolutePath = path.resolve(filePath);
        console.log('Resolved absolute path:', absolutePath);
        const data = fs.readFileSync(absolutePath, 'utf8');
        console.log('File content:', data);
        return data;
    } catch (error) {
        if (error instanceof Error) {
            console.error(`Error reading file: ${error.message}`);
            vscode.window.showErrorMessage(`Error reading file: ${error.message}`);
            throw error;
        } else {
            console.error('Unknown error', error);
            vscode.window.showErrorMessage('An unknown error occurred while reading the file.');
            throw new Error('Unknown error occurred while reading the file.');
        }
    }
}

/**
 * Converts a Markdown string to HTML.
 * 
 * @param {string} markdown - The Markdown content to convert.
 * @returns {string | Promise<string>} - The HTML content.
 */
function convertMarkdownToHtml(markdown: string): string | Promise<string> {
    return marked(markdown);
}
