from requests_html import HTMLSession
import pandas as pd


def get_info(name, purpose, times):
    for time in range(times):
        session = HTMLSession()
        url = 'http://3.95.249.159:8000/random_company'
        content = session.get(url)
        try:
            i = 1
            while True:
                sector = 'body > ol > li:nth-child(' + str(i) + ')'
                results = content.html.find(sector)
                text = results[0].text.split()
                if text[0] == 'Name:':
                    name.append(' '.join(text[1:]))
                if text[0] == 'Purpose:':
                    purpose.append(' '.join(text[1:]))
                    break
                i = i + 1
        except:
            print("Inappropriate URL at time {0}.".format(time))
            break
    print("Successfully collected data.")


def output_data(name, purpose, filename, existing_file_name: str = None):
    collect_info = pd.DataFrame({'Name': name, 'Purpose': purpose})
    try:
        file = open(filename)
        file.close()
        original_info = pd.read_csv(filename)
        try:
            pd.concat([original_info, collect_info]).to_csv('./' + filename, index=False)
            print("Successfully export data to existing file '{0}'.".format(filename))
        except:
            print("Inappropriate file to augment.")
    except:
        collect_info.to_csv('./' + filename, index=False)
        print("Successfully export data to a new file named '{0}'.".format(filename))


if __name__ == '__main__':
    Name, Purpose = [], []
    get_info(Name, Purpose, 50)
    # can either augment an existing file or does it always create a new one
    output_data(Name, Purpose, 'collected_info.csv')





