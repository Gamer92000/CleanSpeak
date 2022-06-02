pre = """
; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "CleanSpeak"
#define MyAppVersion "1.0"
#define MyAppPublisher "Julian Imhof"
#define MyAppURL "https://julianimhof.de/"

[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={userappdata}\TeamSpeak\Default\extensions\de.julianimhof.cleanspeak
DisableDirPage=yes
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
PrivilegesRequired=lowest
OutputBaseFilename=CleanSpeak
Compression=lzma
SolidCompression=yes
WizardStyle=modern
Uninstallable=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"

[Files]
"""

with open("buildInstaller.iss", "w") as f:
    f.write(pre)
    import os

    directory = r'C:\TeamSpeakTheme\Theme'
    for filename in os.listdir(directory):
        x = os.path.join(directory, filename)
        f.write(f"Source: \"{x}\"; DestDir: \"{{app}}\"; Flags: ignoreversion\n")
