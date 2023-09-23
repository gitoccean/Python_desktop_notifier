from plyer import notification  #1
import time     #2

if __name__ == "__main__" :     #3
    while True:       # 5 used for coninutue running of timeout
      notification.notify(
          title="***  Take Rest  ***",
          message="Rest is vital for better mental health, increased concentration, reduced stress, improved mood and even a better metabolism.",
          app_icon="<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M5 3C3.89543 3 3 3.89543 3 5V11C3 15.1421 6.35786 18.5 10.5 18.5H11.5C14.4049 18.5 16.924 16.8485 18.1698 14.4332C21.465 13.9689 24 11.1376 24 7.71429C24 6.21523 22.7848 5 21.2857 5H19C19 3.89543 18.1046 3 17 3H5ZM11.5 16.5C14.5376 16.5 17 14.0376 17 11V5H5V11C5 14.0376 7.46243 16.5 10.5 16.5H11.5ZM19 7L19 11C19 11.4058 18.9678 11.8042 18.9057 12.1925C20.714 11.5091 22 9.76189 22 7.71429C22 7.3198 21.6802 7 21.2857 7H19Z" fill="black"/>
          <path d="M3 20C2.44772 20 2 20.4477 2 21C2 21.5523 2.44772 22 3 22H19C19.5523 22 20 21.5523 20 21C20 20.4477 19.5523 20 19 20H3Z" fill="black"/>
          </svg>,
          timeout=5
           "
           )        #4 timeout means how many seconds icon holdout
      time.sleep(10)      #6 10sec time period
                     #in command room for continue coming pythonw file name(file.py).
                    # want to close go task manager and stop python file.
