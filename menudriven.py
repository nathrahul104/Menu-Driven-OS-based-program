import os
import pyttsx3
import webbrowser

while True:
    print("welcome to the input based operating system controller")
    print("Hello ! How can I help you ?")
    pyttsx3.speak("Hello ! How can I help you ?")
    
    while True:
        p=input()
       
        
        if("notepad" in p):
            print("Launching notepad !")
            pyttsx3.speak("Launching notepad !")
            os.system("notepad")
            print("You have closed Notepad. Anything else sir?")
            pyttsx3.speak("You have closed Notepad. Anything else sir?")

        elif("chrome" in p):
            print("Launching Google Chrome !")
            pyttsx3.speak("Launching Google Chrome !")
            os.system("chrome")
            print("You have closed Google Chrome. Anything else sir?")
            pyttsx3.speak("You have closed Google Chrome. Anything else sir?")

        elif("control panel" in p):
            print("Launching control panel !")
            pyttsx3.speak("Launching control panel !")
            os.system("control panel")
            print("You have closed control panel. Anything else sir?")
            pyttsx3.speak("You have closed control panel. Anything else sir?")

        elif("cmd" in p) or ("command prompt" in p):
            print("Launching Command Prompt !")
            pyttsx3.speak("Launching Command Prompt !")
            os.system("cmd")
            print("You have closed Command Prompt. Anything else sir?")
            pyttsx3.speak("You have closed Command Prompt. Anything else sir?")

        elif("brave" in p):
            pyttsx3.speak("Launching Brave Browser !")
            os.system("brave")
            pyttsx3.speak("You have closed Brave Browser. Anything else sir?")


        elif("geeks for geeks" in p):
            print("Opening Geeks for Geeks on Google chrome !")
            pyttsx3.speak("Opening Geeks for Geeks on Google chrome !")
            url = 'https://www.geeksforgeeks.org/'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            print("You have closed Geeks for Geeks on Google Chrome. Anything else sir ?")
            pyttsx3.speak("You have closed Geeks for Geeks on Google Chrome. Anything else sir ?")

        elif("youtube" in p):
            print("Opening Youtube on Google chrome !")
            pyttsx3.speak("Opening Youtube on Google chrome !")
            url = 'https://www.youtube.com/'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            print("You have closed Youtube on Google Chrome. Anything else sir ?")
            pyttsx3.speak("You have closed Youtube on Google Chrome. Anything else sir ?")
            
        elif("gmail" in p) or ("email" in p):
            print("Opening Gmail on Google chrome !")
            pyttsx3.speak("Opening Gmail on Google chrome !")
            url = ' ((put your gmail link)) '
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            print("You have closed Gmail on Google Chrome. Anything else sir ?")
            pyttsx3.speak("You have closed Gmail on Google Chrome. Anything else sir ?")

        elif("compose" in p):
            print("Opening Gmail -> Compose on Google chrome !")
            pyttsx3.speak("Opening Gmail -> Compose on Google chrome !")
            url = ' ((put your gmail link -> inbox?compose=new)) '
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            print("You have closed Gmail -> Compose on Google Chrome. Anything else sir ?")
            pyttsx3.speak("You have closed Gmail -> Compose on Google Chrome. Anything else sir ?")



        elif("Task Manager" in p) or ("task manager" in p):
            print("Launching Task Manager !")
            pyttsx3.speak("Launching Task Manager !")
            os.system("taskmgr")
            print("You have closed Task Manager. Anything else sir?")
            pyttsx3.speak("You have closed Task Manager. Anything else sir?")

        elif("date" in p):
            print("Today's date is ")
            pyttsx3.speak("Today's date is ")
            os.system("date /t")
            print("Anything else sir?")
            pyttsx3.speak("Anything else sir?")
        
        elif("files and folders" in p):
            print("Executing Command !")
            pyttsx3.speak("Executing Command !")
            os.system("dir")
            print("Anything else sir?")
            pyttsx3.speak("Anything else sir?")

        elif("ip address" in p):
            print("Executing Command !")
            pyttsx3.speak("Executing Command !")
            os.system("ipconfig")
            print("Anything else sir?")
            pyttsx3.speak("Anything else sir?")

        elif("calculator" in p):
            pyttsx3.speak("Showing the recent calender")
            os.system("calc")
            pyttsx3.speak("Anything else sir?")
        
        elif("exit" in p):
            pyttsx3.speak("Thankyou for using the Application")
            break;
        else:
            pyttsx3.speak("Thankyou for using the Application")
        
        
