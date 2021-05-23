
# redirect-lister 🔄

The redirect-lister detects the redirections for URLs given in the text file as input and transfers them to the CSV file in a suitable format. 


## Arguments

redirect-lister works with 3 arguments:

- **-f (--url_file):** Txt file contains target URL's.
- **-c (--count):** How many requests has to made before writing to csv.
- **-h (--help):** For the 'help' menu that you can see the screenshot below. 

Let's say you have thousands of URL's in 'links.txt' file. Therefore, you may want to check the outputs from time to time. With '-c' option, you can specify the number of requests before writing to csv.

**redirect-lister** waits for 5 seconds each time it writes to csv. Which means: **5 seconds break every -c requests**. 

## Example Usage

Given URL's in 'links.txt', csv-writing functionality set to every 50 requests.

```bash
py redirect_lister.py -f links.txt -c 50
```

  
## Help menu 👼

![Help menu](https://i.ibb.co/y4gDMSs/Screenshot-407.png)

  