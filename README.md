# Sandals Resorts 7-7-7

Excited every Wednesday for the Sandals Resorts new 7-7-7 deals to be updated on Sandals website?

This Python scipt will extract and print the Sandals report code along with the Sandals Room Code for the 7-7-7 deals that are listed on their [website](https://www.sandals.com/specials/?scroll=best-value-suites) - sandals.com !

## Requirements

An excel file with `Start Date` entered into cell A1 and `End Date` entered into cell B1

Update the `excel_file_path` variable in the `sandals7-7-7.py` file so that the file location and filename are correct

Pyhton3

This script utilizes the `selenium`, `webdirver_manager`, and `pandas` modules

## To run the script

```
$ python3 sandals7-7-7.py
```
Example output:

```
BEST_VALUE_SUITES Promotions:
Start Date: 2024-12-25, End Date: 2024-12-31, Resort Code: SGO, Room Code: NV1
Start Date: 2024-12-25, End Date: 2024-12-31, Resort Code: SRB, Room Code: VPP
Start Date: 2024-12-25, End Date: 2024-12-31, Resort Code: SWH, Room Code: IVS
Start Date: 2024-12-25, End Date: 2024-12-31, Resort Code: BRP, Room Code: LR
Start Date: 2024-12-25, End Date: 2024-12-31, Resort Code: SLU, Room Code: RP1
Start Date: 2024-12-25, End Date: 2024-12-31, Resort Code: SRC, Room Code: HJS
Start Date: 2024-12-25, End Date: 2024-12-31, Resort Code: SCR, Room Code: KB
```

## Sandals Resort Codes

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