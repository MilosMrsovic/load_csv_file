import requests

def get_missing_data(title, author):
 
    print(f'[INFO] Searching for: {title} - {author}')
 
    url = "https://openlibrary.org/search.json"
    params = {"title": title, "author": author}
 
    try:
 
        response = requests.get(url=url, params=params)
        data = response.json()
 
        if "error" in data:
            print(data['error'])
 
        elif (data["num_found"] > 0):
            first_book = data["docs"][0]
 
            first_sentence = ''
            subject = ''
            place = ''
            time = ''
 
            if "first_sentence" in first_book:
                first_sentence = first_book["first_sentence"]
 
            if "subject" in first_book:
                subject = first_book["subject"]
 
            if "place" in first_book:
                place = first_book["place"]
 
            if "time" in first_book:
                time = first_book["time"]
 
            print(f'[INFO] Found data for: {title} - {author}')
 
            return {
                "first_sentence": first_sentence,
                "subject": subject,
                "place": place,
                "time": time
            }
 
        else:
            print('Book not found')
 
    except requests.exceptions.ConnectionError:
        print("Error: The server is unavailable or the URL is invalid.")
    except requests.exceptions.Timeout:
        print("Error: The request has timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Unexpected error:: {e}")
    
