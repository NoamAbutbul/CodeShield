import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as path from 'path';


export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('codeShield.securityCheck', () => {
        const pythonScriptPath = path.join(context.extensionPath, 'main.py');
        const venvPath = path.join(context.extensionPath, 'venv', 'bin', 'python');
        
        console.log("Hello, world!");
        
        exec(`${venvPath} ${pythonScriptPath}`,{ cwd: path.join(context.extensionPath, 'src') }, (err, stdout, stderr) => {
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
