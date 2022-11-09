from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"
    button_main_page_xpath = "//*[@id='_next']/div[1]/div[1]/div/ul[1]/div[1]/div[2]"
    button_players_xpath = "//*[@id='_next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    button_sign_out_xpath = "//*[@id='_next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    button_dev_team_contact_xpath = "//*[@id='_next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    button_add_player_xpath = "//*[@id='_next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    text_players_count_xpath = "//*[@id='_next']/div[1]/main/div[2]/div[1]/div/div[1]"
    img_xpath = "//*[@id='_next']/div[1]/main/div[3]/div[1]/div/div[1]"
    h2_xpath = "//*[@id='_next']/div[1]/main/div[3]/div[2]/div/div/h2"
    h6_xpath = "//*[@id='_next']/div[1]/main/div[3]/div[3]/div/div/h6[1]"
    text_xpath = "//*[@id='_next']/div[1]/main/div[3]/div[1]/div/div[2]/p"
    pass
