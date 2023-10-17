# README: Data Scraping Bot

This Python script is a web scraping bot designed to collect data from a list of URLs specified in a text file. It uses the Selenium library to automate the web scraping process. The collected data is then formatted and saved into JSON files.

## Prerequisites

Before you can use this script, you'll need to have the following dependencies installed:

- Python 3.x
- Selenium
- Chrome WebDriver (for Selenium)
- Chrome browser (for Selenium)

You can install the required Python packages using `pip`:

```bash
pip install selenium webdriver-manager unidecode
```

### Chrome WebDriver Installation

This script uses the Chrome WebDriver for Selenium. You can automatically download and install the WebDriver using the `webdriver-manager` package. It's configured in the script to do this for you. However, make sure you have Google Chrome installed on your machine.

## Usage

1. **Create a Links File**: Create a text file named `links.md` in the same directory as the script. This file should contain a list of URLs you want to scrape, separated by newlines. You can also include special markers to indicate file breaks or the end of scraping. For example:

   ```plaintext
   - Data Set 1
   https://example.com/page1
   https://example.com/page2
   - Data Set 2
   https://example.com/page3
   - END
   https://example.com/page4
   ```

   - Lines starting with a hyphen `-` indicate a new data set and will be used as the filename for the JSON output.
   - Lines starting with `http` are treated as URLs to scrape.
   - The `END` marker indicates the end of scraping.

2. **Run the Script**: Execute the Python script `data_scraper.py` in your terminal:

   ```bash
   python data_scraper.py
   ```

3. **Scraping Process**: The script will start scraping the specified URLs one by one. It will collect data such as heading, description, image URL, and member count (if available) from each URL.

4. **JSON Output**: The scraped data will be saved in JSON files in the `./data` directory. Each data set will be stored in a separate JSON file, named after the data set specified in the links file.

5. **Special Character Handling**: The script handles special characters in data set names by replacing them with underscores in the output file names.

## Example Output

Here's an example of the structure of the JSON output:

```ts
// data_set_1.ts
let index = 0;

const data_set_1 = [
    {
        heading: "Page 1",
        descr: "This is page 1's description.",
        img: "https://example.com/img1.jpg",
        members: "1000",
        href: "https://example.com/page1",
        index: index++,
    },
    {
        heading: "Page 2",
        descr: "This is page 2's description.",
        img: "https://example.com/img2.jpg",
        members: "2000",
        href: "https://example.com/page2",
        index: index++,
    },
];

export default data_set_1;

// data_set_2.ts
let index = 0;

const data_set_2 = [
    {
        heading: "Page 3",
        descr: "This is page 3's description.",
        img: "https://example.com/img3.jpg",
        members: "500",
        href: "https://example.com/page3",
        index: index++,
    },
];

export default data_set_2;
```

## Notes

- The script uses headless Chrome to perform web scraping, which means it runs without displaying a browser window.
- The `unidecode` library is used to remove special characters and ensure file names are valid.

Please note that web scraping may be subject to legal and ethical considerations. Ensure you have the necessary permissions to scrape the websites you target and adhere to their terms of service.