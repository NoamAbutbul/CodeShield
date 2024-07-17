import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as path from 'path';


export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('codeShield.securityCheck', () => {
        const pythonScriptPath = path.join(context.extensionPath, 'main.py');
        
        console.log("Hello, world!");
        
        exec(`python3 ${pythonScriptPath}`, (err, stdout, stderr) => {
            if (err) {
                vscode.window.showErrorMessage(`Error: ${stderr}`);
            } else {
                vscode.window.showInformationMessage(`Output: ${stdout}`);
            }
        });
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
