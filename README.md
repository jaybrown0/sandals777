# Sandals Resorts 7-7-7

Excited every Wednesday for the Sandals Resorts new 7-7-7 deals to be updated on Sandals website?

This Python scipt will extract and print the Sandals report code along with the Sandals Room Code for the 7-7-7 deals that are listed on their [website](https://www.sandals.com/specials/suite-deals/) - sandals.com !

** Sandals 7-7-7 site was redesigned in Jan 2025.  The code has been updated and also **now includes Beaches 7-7-7 deals** in the ouput!

## Requirements

An excel file with `Start Date` entered into cell A1 

Update the `excel_file_path` variable in the `sandals7-7-7.py` file so that the file location and filename are correct

Pyhton3

This script utilizes the `BeautifulSoup`, `openpyxl`, and `pandas` modules

## To run the script

```
$ python3 sandals7-7-7.py
```
Example output:

```
Today's Extracted Promotions (Sorted by rstCode):

                        promotionTitle rstCode roomCategory
0   7-7-7 Savings - 62% Off Rack Rates     BBO         LOVK
1   7-7-7 Savings - 67% Off Rack Rates     BBO          OTD
2   7-7-7 Savings - 67% Off Rack Rates     BNG          WBS
3   7-7-7 Savings - 62% Off Rack Rates     BNG          BCK
4   7-7-7 Savings - 57% Off Rack Rates     BRP          PRR
5   7-7-7 Savings - 72% Off Rack Rates     BTC          I1B
6   7-7-7 Savings - 72% Off Rack Rates     BTC          2BG
7   7-7-7 Savings - 72% Off Rack Rates     BTC           R2
8   7-7-7 Savings - 62% Off Rack Rates     SCR           KB
9   7-7-7 Savings - 72% Off Rack Rates     SGO          NPV
10  7-7-7 Savings - 67% Off Rack Rates     SLU          B2P
11  7-7-7 Savings - 72% Off Rack Rates     SRB         V1PP
12  7-7-7 Savings - 72% Off Rack Rates     SRC          BBT
13  7-7-7 Savings - 67% Off Rack Rates     SWH         LSUP
```

## Sandals and Beaches Resort Codes

| Resort Code   | Resort |
| ------------- | ------ |
|SBR            | Sandals Royal Barbados |
|SBD            | Sandals Barbados |
|SAT            | Sandals Antigua |
|SGL            | Sandals Grande St Lucia |
|SLS            | Sandals Grenada |
|SHC            | Sandals Halcyon - St Lucia |
|SMB            | Sandals Montego Bay |
|SNG            | Sandals Negril |
|SGO            | Sandals Ochi |
|SLU            | Sandals La Toc - St Lucia |
|SRB            | Sandals Royal Bahamian - Nassau |
|SRC            | Sandals Royal Caribbean - Montego Bay |
|BRP            | Sandals Royal Plantation - Ochos Rio |
|SWH            | Sandals South Coast - Whitehouse Jamaica |
|SCR            | Sandals Curacao |
|SSV            | Sandals Saint Vincent |
|SDR            | Sandals Dunn's River |
|               |                       |
|BBO            | Beaches Ochos Rios |
|BTC            | Beaches Turks and Caicos |
|BNG            | Beaches Negril |