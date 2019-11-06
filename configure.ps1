$extPackages = @(
  '2gua.rainbow-brackets',
  'PKief.material-icon-theme',
  'dracula-theme.theme-dracula',
  'eamodio.gitlens',
  'octref.vetur',
  'oderwat.indent-rainbow',
  'riccardoNovaglia.missinglineendoffile',
  'shardulm94.trailing-spaces',
  'mjmcloug.vscode-elixir',
  'aaron-bond.better-comments'
)

$homeFolder = $env:USERPROFILE
$codeFolder = $homeFolder + '\AppData\Roaming\Code\User'

function InstallExtensions {
  foreach ($package in $extPackages) {
    $command = "code.cmd --install-extension " + $package
    iex $command
  }
}

function OpenFontsFolder {
  echo '--------------------------------'
  echo 'Do manual install fonts included in folder! I really wont waste my time calling WS registers'
  echo '--------------------------------'
  iex 'explorer.exe .\fonts'
}

function CopyPreferencesIntoCodeFolder {
  echo 'Sending profile preferences...'
  Copy-Item './preferences/keybindings.json' -Destination $codeFolder
  Copy-Item './preferences/settings.json' -Destination $codeFolder
}

if(Get-Command code.cmd) {
  InstallExtensions
  OpenFontsFolder
  CopyPreferencesIntoCodeFolder
  echo '--------------------------------'
  echo 'VSCode Ready!'
  echo '--------------------------------'
} else {
  echo 'Please install VSCode, getting from: https://code.visualstudio.com'
}
