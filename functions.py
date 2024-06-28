import webbrowser
import subprocess
from aiogram.types import Message
import psutil

"""runnig or not"""
def is_app_run(app_name):
    for proc in psutil.process_iter(['name']):
        if app_name == proc.info['name']:
            print('chrome yest')
        else:
            print('chrome none')
    
def all_running_apps():
    for proc in psutil.process_iter(['name']):
        print(proc.info['name'])




"""presets"""
def open_edge():
    bsu_url = r"https://bsuedu.ru/bsu/education/schedule/groups/index.php?group=90002296"
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open(bsu_url)
    
    
def open_chrome():
    bsu_url = r"https://bsuedu.ru/bsu/education/schedule/groups/index.php?group=90002296"
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    urls = [
        bsu_url, 
        r"https://www.youtube.com/", 
        r"https://chatgpt.com/"
    ]
    for url in urls:
        webbrowser.get('chrome').open_new_tab(url)
   
   
"""games"""       
def open_dying_lite():
    game_path = r"C:\games\Dying Lite 2\Dying Light 2 Stay Human Reloaded Edition\ph\work\bin\x64\DyingLightGame_x64_rwdi.exe"
    working_directory = r"C:\games\Dying Lite 2\Dying Light 2 Stay Human Reloaded Edition\ph\work\bin\x64"   
    subprocess.run([game_path], cwd = working_directory) 
     

def open_ghost_thusima(): 
    game_path = r"C:\caphead\Ghost.of.Tsushima.Directors.Cut-InsaneRamZes\GhostOfTsushima.exe"
    working_directory = r"C:\caphead\Ghost.of.Tsushima.Directors.Cut-InsaneRamZes"
    subprocess.run([game_path], cwd=working_directory)



"""apps"""       
def open_discord():
    command_to_discord = r'C:\games\Discord\Discord\Update.exe --processStart Discord.exe'
    process = subprocess.Popen(['powershell.exe', '-Command', command_to_discord], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
            print(f"Command '{command_to_discord}' failed with error code {process.returncode}.")
            if stderr:
                print("Error output:")
                print(stderr)
    else:
            print("Output:")
            print(stdout)

def open_steam(): 
    subprocess.run([r"C:\steam\Steam.exe"])      


"""editors"""
def open_visual_studio():
    visual_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe"
    subprocess.run(visual_path)

def open_vs_code():
    vs_code_path = r"C:\studio code\Microsoft VS Code\Code.exe"
    subprocess.run(vs_code_path)

def open_unreal():
    unreal_path = r"C:\unreal\UE_5.3\Engine\Binaries\Win64\UnrealEditor.exe"
    subprocess.run(unreal_path)
    
def open_aseprite():
    aseprite_path = r"C:\aseprite\Aseprite.v1.3.rc4\aseprite.exe"
    subprocess.run(aseprite_path)


"""music"""
def music_drughill():
    url_hills = r"https://music.yandex.ru/artist/5608970"
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url_hills)
    
                        