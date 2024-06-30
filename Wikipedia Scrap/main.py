import requests
import pandas as pd
from bs4 import BeautifulSoup

import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_values_from_url(url):
    # Send an HTTP GET request to the URL and get the response
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the HTML content of the page
        html_content = response.text

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table with class "infobox vcard"
        table = soup.find('table', class_='infobox vcard')

        # Check if the table exists
        if table:
            # Find all 'td' elements within the table and extract their text
            td_elements = table.find_all('td')
            values = [td.get_text(strip=True) for td in td_elements]
            return values
        else:
            print(f"No 'infobox vcard' table found for {url}")
            return None

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

# List of Wikipedia page URLs
links_list = ['https://en.wikipedia.org/wiki/3Hz', 'https://en.wikipedia.org/wiki/A.C.G.T', 'https://en.wikipedia.org/wiki/A.P.P.P.', 'https://en.wikipedia.org/wiki/Anime_International_Company', 'https://en.wikipedia.org/wiki/Ajia-do_Animation_Works', 'https://en.wikipedia.org/wiki/Arvo_Animation', 'https://en.wikipedia.org/wiki/Asahi_Production', 'https://en.wikipedia.org/wiki/Ashi_Productions', 'https://en.wikipedia.org/wiki/Asread', 'https://en.wikipedia.org/wiki/AXsiZ', 'https://en.wikipedia.org/wiki/Bibury_Animation_Studios', 'https://en.wikipedia.org/wiki/Bones_(studio)', 'https://en.wikipedia.org/wiki/Brain%27s_Base', 'https://en.wikipedia.org/wiki/Bridge_(studio)', 'https://en.wikipedia.org/wiki/C-Station', 'https://en.wikipedia.org/wiki/C2C_(studio)', 'https://en.wikipedia.org/wiki/Cloud_Hearts', 'https://en.wikipedia.org/wiki/CoMix_Wave_Films', 'https://en.wikipedia.org/wiki/Creators_in_Pack', 'https://en.wikipedia.org/wiki/Diomed%C3%A9a', 'https://en.wikipedia.org/wiki/Doga_Kobo', 'https://en.wikipedia.org/wiki/Egg_Firm', 'https://en.wikipedia.org/wiki/Eight_Bit_(studio)', 'https://en.wikipedia.org/wiki/Ekachi_Epilka', 'https://en.wikipedia.org/wiki/Haoliners_Animation_League', 'https://en.wikipedia.org/wiki/EMT_Squared', 'https://en.wikipedia.org/wiki/Encourage_Films', 'https://en.wikipedia.org/wiki/Ezo%27la', 'https://en.wikipedia.org/wiki/Felix_Film', 'https://en.wikipedia.org/wiki/Frontier_Works', 'https://en.wikipedia.org/wiki/Gainax', 'https://en.wikipedia.org/wiki/Gallop_(studio)', 'https://en.wikipedia.org/wiki/Genco', 'https://en.wikipedia.org/wiki/Gathering_(animation_studio)', 'https://en.wikipedia.org/wiki/G%26G_Entertainment', 'https://en.wikipedia.org/wiki/GoHands', 'https://en.wikipedia.org/wiki/Grizzly_(studio)', 'https://en.wikipedia.org/wiki/Hoods_Entertainment', 'https://en.wikipedia.org/wiki/Imagin_(studio)', 'https://en.wikipedia.org/wiki/J.C.Staff', 'https://en.wikipedia.org/wiki/Khara_(studio)', 'https://en.wikipedia.org/wiki/Kinema_Citrus', 'https://en.wikipedia.org/wiki/Kyoto_Animation', 'https://en.wikipedia.org/wiki/Lapin_Track', 'https://en.wikipedia.org/wiki/Lesprit', 'https://en.wikipedia.org/wiki/Magic_Bus_(studio)', 'https://en.wikipedia.org/wiki/Maho_Film', 'https://en.wikipedia.org/wiki/MAPPA', 'https://en.wikipedia.org/wiki/Marvelous_(company)', 'https://en.wikipedia.org/wiki/Movic', 'https://en.wikipedia.org/wiki/Millepensee', 'https://en.wikipedia.org/wiki/NAZ_(studio)', 'https://en.wikipedia.org/wiki/Nexus_(animation_studio)', 'https://en.wikipedia.org/wiki/Nippon_Animation', 'https://en.wikipedia.org/wiki/Nomad_(company)', 'https://en.wikipedia.org/wiki/NUT_(studio)', 'https://en.wikipedia.org/wiki/Odessa_Entertainment', 'https://en.wikipedia.org/wiki/Oh!_Production', 'https://en.wikipedia.org/wiki/Okuruto_Noboru', 'https://en.wikipedia.org/wiki/Orange_(animation_studio)', 'https://en.wikipedia.org/wiki/P.A._Works', 'https://en.wikipedia.org/wiki/Passione_(company)', 'https://en.wikipedia.org/wiki/Pierrot_(company)', 'https://en.wikipedia.org/wiki/Pine_Jam', 'https://en.wikipedia.org/wiki/Platinum_Vision', 'https://en.wikipedia.org/wiki/Polygon_Pictures', 'https://en.wikipedia.org/wiki/Project_No.9', 'https://en.wikipedia.org/wiki/Satelight', 'https://en.wikipedia.org/wiki/Science_Saru', 'https://en.wikipedia.org/wiki/Seven_(animation_studio)', 'https://en.wikipedia.org/wiki/Shaft_(company)', 'https://en.wikipedia.org/wiki/Shirogumi', 'https://en.wikipedia.org/wiki/Shuka_(studio)', 'https://en.wikipedia.org/wiki/Sola_Digital_Arts', 'https://en.wikipedia.org/wiki/Studio_4%C2%B0C', 'https://en.wikipedia.org/wiki/Studio_A-Cat', 'https://en.wikipedia.org/wiki/Studio_Blanc', 'https://en.wikipedia.org/wiki/Studio_Chizu', 'https://en.wikipedia.org/wiki/Studio_Comet', 'https://en.wikipedia.org/wiki/Studio_Deen', 'https://en.wikipedia.org/wiki/Studio_Flad', 'https://en.wikipedia.org/wiki/Studio_Ghibli', 'https://en.wikipedia.org/wiki/Studio_Gokumi', 'https://en.wikipedia.org/wiki/Studio_Nue', 'https://en.wikipedia.org/wiki/Studio_Palette', 'https://en.wikipedia.org/wiki/Studio_Ponoc', 'https://en.wikipedia.org/wiki/Studio_Puyukai', 'https://en.wikipedia.org/wiki/Studio_VOLN', 'https://en.wikipedia.org/wiki/Tezuka_Productions', 'https://en.wikipedia.org/wiki/TNK_(company)', 'https://en.wikipedia.org/wiki/Troyca', 'https://en.wikipedia.org/wiki/Typhoon_Graphics', 'https://en.wikipedia.org/wiki/Ufotable', 'https://en.wikipedia.org/wiki/White_Fox', 'https://en.wikipedia.org/wiki/Wolfsbane_(animation_studio)', 'https://en.wikipedia.org/wiki/Yokohama_Animation_Laboratory', 'https://en.wikipedia.org/wiki/Zero-G_(studio)', 'https://en.wikipedia.org/wiki/Asahi_Broadcasting_Corporation', 'https://en.wikipedia.org/wiki/Silver_Link', 'https://en.wikipedia.org/wiki/Asatsu-DK', 'https://en.wikipedia.org/wiki/Gonzo_(company)', 'https://en.wikipedia.org/wiki/Nihon_Ad_Systems', 'https://en.wikipedia.org/wiki/Studio_Kai', 'https://en.wikipedia.org/wiki/Bandai_Namco_Holdings', 'https://en.wikipedia.org/wiki/Bandai_Namco_Filmworks', 'https://en.wikipedia.org/wiki/Studio_Mother', 'https://en.wikipedia.org/wiki/Happinet', 'https://en.wikipedia.org/wiki/CyberAgent', 'https://en.wikipedia.org/wiki/Digital_Frontier', 'https://en.wikipedia.org/wiki/Fanworks_(animation_studio)', 'https://en.wikipedia.org/wiki/Feel_(animation_studio)', 'https://en.wikipedia.org/wiki/Fuji_TV', 'https://en.wikipedia.org/wiki/David_Production', 'https://en.wikipedia.org/wiki/Gaina_(company)', 'https://en.wikipedia.org/wiki/Geek_Pictures', 'https://en.wikipedia.org/wiki/Graphinica', 'https://en.wikipedia.org/wiki/IG_Port', 'https://en.wikipedia.org/wiki/Signal.MD', 'https://en.wikipedia.org/wiki/Wit_Studio', 'https://en.wikipedia.org/wiki/Imagica', 'https://en.wikipedia.org/wiki/Robot_Communications', 'https://en.wikipedia.org/wiki/Kadokawa_Corporation', 'https://en.wikipedia.org/wiki/ENGI', 'https://en.wikipedia.org/wiki/Nintendo', 'https://en.wikipedia.org/wiki/Nippon_TV', 'https://en.wikipedia.org/wiki/Tatsunoko_Production', 'https://en.wikipedia.org/wiki/Sega_Sammy_Holdings', 'https://en.wikipedia.org/wiki/Telecom_Animation_Film', 'https://en.wikipedia.org/wiki/Sony_Music_Entertainment_Japan', 'https://en.wikipedia.org/wiki/CloverWorks', 'https://en.wikipedia.org/wiki/Square_Enix', 'https://en.wikipedia.org/wiki/Studio_Bind', 'https://en.wikipedia.org/wiki/Studio_Hibari', 'https://en.wikipedia.org/wiki/Lerche_(brand)', 'https://en.wikipedia.org/wiki/Tokyo_Broadcasting_System', 'https://en.wikipedia.org/wiki/Toei_Company', 'https://en.wikipedia.org/wiki/TV_Asahi', 'https://en.wikipedia.org/wiki/Twin_Engine_(company)', 'https://en.wikipedia.org/wiki/Lay-duce', 'https://en.wikipedia.org/wiki/Revoroot', 'https://en.wikipedia.org/wiki/Studio_Colorido', 'https://en.wikipedia.org/wiki/Ultra_Super_Pictures', 'https://en.wikipedia.org/wiki/Sanzigen', 'https://en.wikipedia.org/wiki/Studio_Trigger', 'https://en.wikipedia.org/wiki/Zexcs', 'https://en.wikipedia.org/wiki/Artland_(company)', 'https://en.wikipedia.org/wiki/Bee_Train_Production', 'https://en.wikipedia.org/wiki/Chaos_Project', 'https://en.wikipedia.org/wiki/Daume', 'https://en.wikipedia.org/wiki/Knack_Productions', 'https://en.wikipedia.org/wiki/Mook_Animation', 'https://en.wikipedia.org/wiki/Mushi_Production', 'https://en.wikipedia.org/wiki/Ordet_(studio)', 'https://en.wikipedia.org/wiki/Remic', 'https://en.wikipedia.org/wiki/Zuiyo', 'https://en.wikipedia.org/wiki/Arms_(company)', 'https://en.wikipedia.org/wiki/Artmic', 'https://en.wikipedia.org/wiki/Bandai_Visual', 'https://en.wikipedia.org/wiki/Group_TAC', 'https://en.wikipedia.org/wiki/Hal_Film_Maker', 'https://en.wikipedia.org/wiki/J2_Communications', 'https://en.wikipedia.org/wiki/Kitayama_Eiga_Seisakujo', 'https://en.wikipedia.org/wiki/Kitty_Films', 'https://en.wikipedia.org/wiki/Kokusai_Eiga-sha', 'https://en.wikipedia.org/wiki/Manglobe', 'https://en.wikipedia.org/wiki/Palm_Studio', 'https://en.wikipedia.org/wiki/Production_IMS', 'https://en.wikipedia.org/wiki/Radix_Ace_Entertainment', 'https://en.wikipedia.org/wiki/Spectrum_Animation', 'https://en.wikipedia.org/wiki/Studio_Fantasia', 'https://en.wikipedia.org/wiki/Tear_Studio', 'https://en.wikipedia.org/wiki/Topcraft', 'https://en.wikipedia.org/wiki/Triangle_Staff', 'https://en.wikipedia.org/wiki/Tsuchida_Production', 'https://en.wikipedia.org/wiki/List_of_animation_studios_owned_by_The_Walt_Disney_Company#Disney_Animation_Japan', 'https://en.wikipedia.org/wiki/Xebec_(studio)', 'https://en.wikipedia.org/wiki/Yaoyorozu']


# Create an empty list to store the DataFrames
data_frames_list = []

# Process each link and store the results in a list of DataFrames
for link in links_list:
    values = extract_values_from_url(link)
    if values:
        # Create a Series from the extracted values and add it to the list
        print(values)
        series = pd.Series(values, name=link)
        data_frames_list.append(series)

# Concatenate all the DataFrames into a single DataFrame
result_df = pd.DataFrame(data_frames_list)

# Print the final DataFrame
result_df.to_csv('output_data.csv', index=False)
