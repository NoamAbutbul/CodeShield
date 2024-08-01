import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('codeShield.securityCheck', () => {
        const pythonScriptPath = path.join(context.extensionPath, 'main.py');
        const venvPath = path.join(context.extensionPath, 'venv', 'bin', 'python');

        // Get the user's workspace directory
        const workspaceFolders = vscode.workspace.workspaceFolders;
        
        if (!workspaceFolders || workspaceFolders.length === 0) {
            vscode.window.showErrorMessage('No workspace folder open.');
            console.log('No workspace folders found.');
            return;
        }

        const workspacePath = workspaceFolders[0].uri.fsPath;
        console.log('Workspace path:', workspacePath);

        const options = {
            cwd: context.extensionPath  // Set the current working directory to the extension's root directory
        };

        exec(`${venvPath} ${pythonScriptPath} ${workspacePath}`, options, (err, stdout, stderr) => {
            if (err) {
                vscode.window.showErrorMessage(`Error: ${err.message}`);
                console.log(`Error: ${err.message}`);
            } else {
                vscode.window.showInformationMessage(`Output: ${stdout}`);
                console.log(`Output: ${stdout}`);
            }
        });
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}