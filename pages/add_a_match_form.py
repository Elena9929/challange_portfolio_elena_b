from pages.base_page import BasePage


class Dashboard(BasePage):
 input_xpath = "//*[@id='_next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
 input_enemy_team_xpath = "//*[@id='next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
 input_enemy_team_score_xpath = "//*[@id='next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
 input_league_xpath = "//*[@id='next']/div[1]/main/div[2]/form/div[2]/div/div[8]/div/div/input"
 input_number_xpath = "//*[@id='_next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
 input_general_xpath = "//*[@id='_next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
 input_radio_xpath = "//*[@id='_next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[1]/span[1]/input"
 button_matches_xpath = "//*[@id='_next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
 button_leanguage_xpath = "//*[@id='_next']/div[1]/div/div/div/ul[3]/div[1]/div[2]/span"
 button_submit_xpath = "//*[@id='_next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"
 pass
