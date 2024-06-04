# import pandas as pd
# import os
# from dotenv import load_dotenv
# load_dotenv()

# twitter_auth_token= os.getenv("TWITTER_AUTH_TOKEN")

# def scrape_twitter_data(search_keywords, filename, limit, twitter_auth_token):
#     for keyword in search_keywords:
#         !npx -y tweet-harvest@2.6.1 -o "{filename}" -s "{keyword}" --tab "LATEST" -l {limit} --token {twitter_auth_token}

# def remove_duplicates_and_add_column(filename):
#     file_path = f"tweets-data/{filename}"
#     df = pd.read_csv(file_path, delimiter=",")
#     df['jenis_program'] = 'Program Indonesia Pintar (PIP)'
#     df.drop_duplicates(inplace=True)
#     df.to_csv(f'scrapped_{filename}', index=False)

# # Keyword list
# search_keywords = ['PIP lang:id since:2024-01-01', 'Program Indonesia Pintar lang:id since:2024-01-01', 'Kartu Indonesia Pintar lang:id since:2024-01-01', 'KIP lang:id since:2024-01-01',
#                    'kip lang:id since:2024-01-01','pip lang:id since:2024-01-01']
# filename = 'kemensos.csv'
# limit = 500


# # Scrape Twitter data for each keyword
# scrape_twitter_data(search_keywords, filename, limit, twitter_auth_token)

# # Remove duplicates and add column for each scrapped file
# remove_duplicates_and_add_column(filename)

# import pandas as pd
# import os
# import subprocess
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Get Twitter authentication token from environment variables
# twitter_auth_token = os.getenv("TWITTER_AUTH_TOKEN")

# def scrape_twitter_data(search_keywords, filename, limit, twitter_auth_token):
#     for keyword in search_keywords:
#         command = [
#             'npx', '-y', 'tweet-harvest@2.6.1', '-o', filename,
#             '-s', keyword, '--tab', 'LATEST', '-l', str(limit),
#             '--token', twitter_auth_token
#         ]
#         subprocess.run(command, check=True)

# def remove_duplicates_and_add_column(filename):
#     file_path = f"tweets-data/{filename}"
#     df = pd.read_csv(file_path, delimiter=",")
#     df['jenis_program'] = 'Program Indonesia Pintar (PIP)'
#     df.drop_duplicates(inplace=True)
#     df.to_csv(f'scrapped_{filename}', index=False)

# # Keyword list
# search_keywords = [
#     'PIP lang:id since:2024-01-01', 'Program Indonesia Pintar lang:id since:2024-01-01',
#     'Kartu Indonesia Pintar lang:id since:2024-01-01', 'KIP lang:id since:2024-01-01',
#     'kip lang:id since:2024-01-01', 'pip lang:id since:2024-01-01'
# ]
# filename = 'kemensos.csv'
# limit = 500

# # Scrape Twitter data for each keyword
# scrape_twitter_data(search_keywords, filename, limit, twitter_auth_token)

# # Remove duplicates and add column for each scrapped file
# remove_duplicates_and_add_column(filename)
