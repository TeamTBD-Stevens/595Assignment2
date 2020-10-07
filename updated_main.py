from requests_html import HTMLSession
import pandas as pd
import sys


def get_info(url: str, times):
    name, purpose = [], []
    for time in range(times):
        session = HTMLSession()
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
            sys.stderr.write("Inappropriate URL at time {0}.".format(time))
            exit(1)
    print("Successfully collected data.")
    collect_info = pd.DataFrame({'Name': name, 'Purpose': purpose})
    return collect_info


def output_data(collect_info, filename):
    try:
        file = open(filename)
        file.close()
        original_info = pd.read_csv(filename)
        try:
            pd.concat([original_info, collect_info]).to_csv('./' + filename, index=False)
            print("Successfully export data to existing file '{0}'.".format(filename))
        except:
            sys.stderr.write('Inappropriate file to augment')
    except:
        collect_info.to_csv('./' + filename, index=False)
        print("Successfully export data to a new file named '{0}'.".format(filename))


if __name__ == '__main__':
    collect_info_df = get_info('http://3.95.249.159:8000/random_company', 50)
    # can either augment an existing file or create a new one
    output_data(collect_info_df, 'collected_info.csv')





