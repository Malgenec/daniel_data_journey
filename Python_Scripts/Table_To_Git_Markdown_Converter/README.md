# TTGConverter

TTGConverter or Table To GitHub (markdown) Converter.

A very simple Python-based GUI tool to convert tab-separated SQL results into GitHub-style Markdown table.

It was made for my own uses to shorten the time logging my learning progress at SQL.

## Features

- Paste tabular data (e.g. SQL/Excel/Git Markdown (preview versions) copy-paste)
- Format (via Process button) the input text into a clean markdown table
- Adjusts column width dynamically for neat alignment
- Copy, download to .txt or print the result to the console
- Remove quotes (both from headers and the data)
- Make headers start with the capital letter
- View output console for debugging

## Screenshot

![Alt text](/daniel_data_journey/Python_Scripts/Table_To_Git_Markdown_Converter/display_window.png?raw=true "Screenshot from the TTGConverter v1.0")

## How to run

You can run this tool in two ways: as a Python script or as a compiled `.exe.` file

### Run from Python

Make sure you have Python installed:

Simply open it up (not in the editor) or

```
python TTGConverter.py
```

If you don't have dependencies like `tkinter` or `pyperclip`, install them:

```
pip install tkinter
```

```
pip install pyperclip
```

### Build an .exe (Windows)

You can compile the tool into a standalone executable using PyInstaller:

```
pip install pyinstaller

pyinstaller --onefile --windowed TTGConverter.py
```

The executable will appear in the dist/ folder.

## File Structure

`TTGConverter.py`     Main GUI script

`README.md`           Project description

`LICENSE`             Open-source license

## Example Input & Output

### Input:

```
"name"	"concentration"	"quantity"	"manufacturer"
"Nitric Acid"	68	13	"Sigma-Aldrich"
"Ethanol"	50	69	"Neighbour"
"NaCl"	100	454	"Mother Earth"
"Sulfuric Acid"	32	2	"Sigma-Aldrich"
"Phosphoric Acid"	40	34	"Sigma-Aldrich"
"Uranium"	100	9001	"Neighbour"
"Hydrochloric Acid"	37	10	"Sigma-Aldrich"
"Potassium Iodide"	5	25	"LabSource"
"Sodium Hydroxide"	50	100	"Sigma-Aldrich"
"Methanol"	99	500	"Neighbour"
"Acetone"	100	250	"Mother Earth"
"Ammonium Nitrate"	60	300	"LabSource"
"Copper Sulfate"	20	150	"Sigma-Aldrich"
"Zinc Powder"	95	75	"Neighbour"
"Calcium Carbonate"	80	200	"EarthWorks"
"Phenolphthalein"	1	5	"Sigma-Aldrich"
```

### Output:

(with `Remove Quotes?` and `Capitalize Headers?` checked)

```
|Name             |Concentration|Quantity|Manufacturer |
|:---------------:|:-----------:|:------:|:-----------:|
|Nitric Acid      |68           |13      |Sigma-Aldrich|
|Ethanol          |50           |69      |Neighbour    |
|NaCl             |100          |454     |Mother Earth |
|Sulfuric Acid    |32           |2       |Sigma-Aldrich|
|Phosphoric Acid  |40           |34      |Sigma-Aldrich|
|Uranium          |100          |9001    |Neighbour    |
|Hydrochloric Acid|37           |10      |Sigma-Aldrich|
|Potassium Iodide |5            |25      |LabSource    |
|Sodium Hydroxide |50           |100     |Sigma-Aldrich|
|Methanol         |99           |500     |Neighbour    |
|Acetone          |100          |250     |Mother Earth |
|Ammonium Nitrate |60           |300     |LabSource    |
|Copper Sulfate   |20           |150     |Sigma-Aldrich|
|Zinc Powder      |95           |75      |Neighbour    |
|Calcium Carbonate|80           |200     |EarthWorks   |
|Phenolphthalein  |1            |5       |Sigma-Aldrich|
```

## Tips and known issues:

- Works only with tab-separated input (SQL editors, excel, some website tables). No function for other separators (yet?)
- Deletes ALL quotes `"`, which means not only in the header, but across data too
- If you want to capitalize the headers and there are quotes `"` in them which you don't want to remove, capitalize function does not work

## TODO

The following list does not mean it will be implemented, because it's a personal project and until there is personal need the tool won't be modified.

- Support other delimiters
- Make the capitalize headers function work even with the existence of quote signs
- Choices for quotes removal for header/data
- Choices for alignment
- Function to clean the console
- Dark mode GUI

## License

This tool is licensed under the MIT License. You are free to use, modify, and distribute it with proper attribution

See the [LICENSE](./LICENSE) file for details.

## Author

Created by Malgenec (Daniel). Feel free to fork :smiley_cat:
