import requests
from bs4 import BeautifulSoup
import pandas as pd

results = []
base_url = "https://www.koreabaseball.com/Record/Retire/Hitter.aspx?playerId="

# 테스트 범위 (나중에 1000 ~ 99999로 변경 가능)
for player_id in range(1000, 99999):
    url = base_url + str(player_id)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        no_record = soup.select_one(
            "#contents > div.sub-content > div.player_records > table.tData01.tt.mb5 > tfoot > tr > td"
        )
        if no_record and "기록이 없습니다." in no_record.text:
            continue

        name_tag = soup.select_one("#cphContents_cphContents_cphContents_ucRetireInfo_lblName")
        if not name_tag:
            continue
        name = name_tag.text.strip()

        pic_tag = soup.select_one("#cphContents_cphContents_cphContents_ucRetireInfo_imgProgile")
        pic_url = "https:" + pic_tag['src'] if pic_tag and 'src' in pic_tag.attrs else ""

        birth_tag = soup.select_one("#cphContents_cphContents_cphContents_ucRetireInfo_lblBirthday")
        birth = birth_tag.text.strip()[:4] if birth_tag else ""

        table_body = soup.select_one("#contents > div.sub-content > div.player_records > table.tData01.tt.mb5 > tbody")
        if not table_body:
            continue
        rows = table_body.find_all("tr")

        for row in rows:
            cols = [col.text.strip() for col in row.find_all("td")]
            if len(cols) < 22:
                continue

            data = {
                "name": name,
                "pic_url": pic_url,
                "birth": birth,
                "season": cols[0],
                "team": cols[1],
                "AVG": cols[2],
                "G": cols[3],
                "PA": cols[4],
                "AB": cols[5],
                "R": cols[6],
                "H": cols[7],
                "2B": cols[8],
                "3B": cols[9],
                "HR": cols[10],
                "TB": cols[11],
                "RBI": cols[12],
                "SB": cols[13],
                "CS": cols[14],
                "BB": cols[15],
                "HBP": cols[16],
                "SO": cols[17],
                "GDP": cols[18],
                "SLG": cols[19],
                "OBP": cols[20],
                "E": cols[21],
            }
            results.append(data)

    except Exception:
        continue

# 저장
df = pd.DataFrame(results)
df.to_csv("retired_kbo_hitters.csv", index=False, encoding='utf-8-sig')
