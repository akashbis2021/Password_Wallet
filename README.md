# Password_Wallet V-0.1

Hi I am Akash Biswas (INDIA)
Password-wallet is my personal projects that I love too share publically. 
This peace of software or script i made for linux Desktop's 
I am loving Linux main line distro and linux User those who are passionate about it.
THANKS TOO ALL WHO TRY MY PROJECT.

LETS START, TO KNOW ABOUT MY PROJECT PASSWORD-WALLET(V.01)
==========================================================
1.This peace of script build in python3
  For GUI Tkinter used 
  
  //IMPORTING//
  =============
  from tkinter import*
  import tkinter as tk
  from tkinter import messagebox
  import random
  import os
  from tkinter import scrolledtext  

2.LOGIN PAGE CONTENT (FRONTEND):-
================================
  i)    USERNAME ENTRY BOX
  ii)   PASSWORD ENTRY BOX
  iii)  SIGN IN BUTTON
  iv)   REGISTER BUTTON
  v)    FORGET PASSWORD? BUTTON
  
3.MAIN CONTENT(BACKEND):-
=======================
  i)    WEBSITE ENTRY BOX
  ii)   EMAIL ENTRY BOX
  iii)  PASSWORD ENTRY BOX WITH RANDOM PASSWORD GENRATOR
  iv)   ADD BUTTON: TO SAVE ENTRIES GIVEN BY THE USER'S IN THE FIELD'S
  v)    ALL ENTIRES BUTTON: TO SHOW ALL ENTIRES
  
4.[.desktop script OF PASSWORD WALLET (PROVIDED) ]
======================================
  HERE pass-wallet.desktop CREATE THE SHORTCUT OF THE SCRIPT WITH LOGO
  THE PURPOSE OF .desktop SCRIPT IF YOU RUN THE PROGRAM DIRECTLY FROM THE DESKTOP
  WITHOUT USING TERMINAL.
  
  PROCEDURE:-
  ===========
  1.pass-wallet.desktop COPY TO /home/username/.local/share/applications DIRECTORY
  
  .desktop CONTENTS/EXPLAIN:-
  ===========================
  # The type as listed above
     Type=Application
 
  # The version of the desktop entry specification to which this file complies
  Version=0.1
 
  # The name of the application
  Name=Passwallet

  # The path to the folder in which the executable is run
  #Path=<FILE PATH WHERE YOU PASSWORDWALLET DIR >     <<   THIS LINE IS ALL LOG FILES STORE IN THE GIVEN PATH

  # The executable of the application, possibly with arguments.
  Exec= < ENTER PATH WHERE YOU PASSWORDWALLET DIR >/passwordwallet.py  << THIS LINE IS THE MAIN SCRIPT   

  # The name of the icon that will be used to display this entry
  Icon= <ENTER PATH WHERE YOU PASSWORDWALLET DIR >/pass-walletlogo.png  << THIS LINE SHOWS ICON ON THE DESKTOP  
 
  # Describes whether this application needs to be run in a terminal or not
  #Terminal=false

   
  
   
  
  
