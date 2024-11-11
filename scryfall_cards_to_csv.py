import requests
import pandas as pd

class Scryfall_Cards:
    print('do Scryfall_Cards.help_params()')

    @staticmethod
    def help_params():
        print('type: creature, cat, dog, instant, enchantment, demon, planeswalker,...')
        print('color: r(red), u(blue), w(white), b(black), g(green), colorless, wg(white and green), br(black and red), ur(blue and red),...')
        print('color=(exclusively that colors)')
        print('cmc=1, <2, >=3,...')
        print('rarity: mythic, common, uncommon,...')
        print('oracle: flying, infect, trample,...')
        print()
        print('Params Example:\n type:creature type:enchantment type:human oracle:lifelink color:gw')

    def __init__(self, card_type):
        self.params = {'q': f'(game:paper) {card_type}'}
        self.api_search_url = 'https://api.scryfall.com/cards/search'
    
    def search_cards(self):
        url = self.api_search_url
        all_cards = []
        while url:
            response = requests.get(url, params = self.params)
            response_json = response.json()
            
            if "data" in response_json:
                all_cards.extend(response_json['data'])
            
            if response_json.get("has_more"):
                url = response_json["next_page"]
            else:
                url = None
        return all_cards

    def card_names(self, cards_request):
         return [card['name'] for card in cards_request]
    
    def card_type_lines(self, cards_request):
        return [card['type_line'] for card in cards_request]
    
    def card_releases(self, cards_request):
        return [card['released_at'] for card in cards_request]

    def card_usd_prices(self, cards_request):
        return [card['prices'].get('usd') for card in cards_request]

    def card_cmcs(self, cards_request):
        return [card['cmc'] for card in cards_request]
        
    def card_raritys(self, cards_request):
        return [card['rarity'] for card in cards_request]
    
    def card_color_identity(self, cards_request):
        return [card['color_identity'] for card in cards_request]
    

    def create_df_cards(self):
        all_cards = self.search_cards()
        names = self.card_names(all_cards)
        type_lines = self.card_type_lines(all_cards)
        releases = self.card_releases(all_cards)
        usd_prices = self.card_usd_prices(all_cards)
        cmcs = self.card_cmcs(all_cards)
        colors_identitys = self.card_color_identity(all_cards)
        raritys = self.card_raritys(all_cards)

        df = pd.DataFrame({'card_name': names, 'card_type': type_lines, 'release': releases, 'usd_price': usd_prices,
                           'cmc': cmcs, 'color_identity': colors_identitys, 'rarity': raritys})
        
        return df