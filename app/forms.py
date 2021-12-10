from django import forms
import json


def readJson(filename):
        with open(filename, 'r',encoding="utf-8_sig") as fp:
            return json.load(fp)


def get_prefecture():
    """ 都道府県を選択する """
    filepath = './static/data/ja_prefecture.json'
    all_data = readJson(filepath)
    prefectures = list(all_data.keys())
    all_prefectures = [('-----', '---都道府県の選択---')]
    for prefecture in prefectures:
        all_prefectures.append((prefecture, prefecture))
    return all_prefectures


def return_cities_by_prefecture(prefecture):
    """ 都道府県の選択を取得  """
    filepath = './static/data/ja_prefecture.json'
    all_data = readJson(filepath)
    #指定の都道府県の市区町村データを取得
    all_cities = all_data[prefecture]
    return all_cities


class AddressForm(forms.Form):
    country = forms.ChoiceField(
                    choices = get_prefecture(),
                    required = False,
                    label='都道府県',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_prefecture'}),
                    )
 