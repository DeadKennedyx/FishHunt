```                                                                                          
            :                             -.                                        
           -:                           :*%: :                                      
           +                     ..::::+%%%*#%-=                                    
          :-                :=+#%%%%%%%%%%%%%%%%#%-=-                    :.         
          +              :+%%%%%%%%%%%%%%%%%%%%%%%%%%#--              :=##          
        -%%:           -#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+#:        .=#%%%-          
        #%%.         .*%%%%%-  :#%%%%*%%%%%%%%%%%%%%%%%%%%%+:   .-*%%%%%%.          
       .##=          -#%%%%%.  .#%%%%%-%%%%%%%%%%%%%%%%%%%%%%%++%%%%%%%%+           
        #.         .   :*%%%%##%%%%%%%-*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.           
       -+         =#     .=%%%%%%%%%%%+-%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+           
       *:        :-%.     .=%%%%%%%%%%=:%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=          
       ==         :*    -*%%%%%%%%%%%%--%%%%%%%%%%%%%%%%%%%%%%#++*#%%%%%%%-         
        *=      .=*   -%%%%%%%%%%%%%%%.*%%%%%%%%%%%%%%%%%%%#+:      ..:-=+*.        
         :++===++:     =%%%%%%%%%%%%%*=%%%%%%%%%%%%%%%%%*=.                         
                        .=%%%%%%%%%%%#%%%%%%%%%%%%%#*=:                             
                           -+#%%%%%%%%%%%%%%%%#*=-.                                 
                              .-==++*+#%%#-:.                                       
                                       +%%.                                         
                                         :-

                            FISHHUNT BY DEADKENNEDYX
```


As of right now FishHunt is a GMAIL phishing detection system, uses a machine learning model trained on 5000 phishing emails and 5000 non-phsishing emails. 

It also uses [MalTrail](https://github.com/stamparm/maltrail?tab=readme-ov-file#blacklist) list of malicious domains that is updated every day and checks the urls in the emails for any of those malicious urls.


### USAGE:

1- `pip3 install -r requirements.txt`.

2- Copy and paste your credentials.json in the root folder from your google oauth client, file name must be `credentials.json`

2- Go to `/FishNet` and run `python3 email_training.py`, this will start the model training with the legal and phishing emails `.mbox`.

3- We will have now 2 file outputs after running the email_training `phishing_model.pkl` and `vectorizer.pkl`.

4- Now go to root folder and run `python3 main.py`, if you have not been logged in before then it will open a browser tab with the gmail auth page

5- After logging in it will create a `token.json` file in the root folder which will be used for further runs of the script without needing to log in each time you run it

5- By default it checks your last 100 emails, you can modify the script `phishing_detection.py` to increase the default, or implement websockets/push-notifications for live tracking
