import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as path from 'path';
import fs from 'fs';


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
                createWebviewPanel(stdout);
            }
        });
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}

function createWebviewPanel(output: string) {
    const panel = vscode.window.createWebviewPanel(
        'codeShieldOutput', // Identifies the type of the webview. Used internally
        'CodeShield Output', // Title of the panel displayed to the user
        vscode.ViewColumn.One, // Editor column to show the new webview panel in
        {} // Webview options
    );

    // Format the output as plain text, replacing HTML tags
    const formattedOutput = formatOutput(output);

    // And set its HTML content
    panel.webview.html = renderTemplate(formattedOutput);
}


function formatOutput(output: string): string {
    return output
        .replace(/<\/?[^>]+(>|$)/g, '') // Remove all HTML tags
        .replace(/(\*\*|<br>|\n)+/g, '\n') // Convert remaining markers to new lines
        .trim(); // Remove leading and trailing whitespace
}




function renderTemplate(output: string): string {
    // Load the HTML template from file
    // const templatePath = path.resolve('output_template/template.html');
    const template = fs.readFileSync('output_template/template.html', 'utf-8');
    
    // Replace the placeholder with the actual output
    const renderedHtml = template.replace('{{output}}', output);

    console.log('html file:', renderedHtml);

    
    return renderedHtml;
}



// function getWebviewContent(output: string): string {
//     // Simple HTML template to display the output
//     return `<!DOCTYPE html>
//     <html lang="en">
//     <head>
//         <meta charset="UTF-8">
//         <meta name="viewport" content="width=device-width, initial-scale=1.0">
//         <title>CodeShield Output</title>
//         <style>
//             body {
//                 font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
//                 padding: 16px;
//                 line-height: 1.6;
//             }
//             pre {
//                 background-color: #f3f3f3;
//                 padding: 32px;
//                 border-radius: 8px;
//             }
//         </style>
//     </head>
//     <body>
//         <pre>${output}</pre>
//     </body>
//     </html>`;
// }
