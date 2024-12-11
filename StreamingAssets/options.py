import pygame
import ctypes, pygame, sys, os, csv
import random
import pandas as pd

class Options:
    def __init__(self):
        
        self.screen = pygame.display.set_mode((1680, 1050), pygame.RESIZABLE)
        self.display_surface = pygame.display.get_surface()
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.click_sound = pygame.mixer.Sound('Audio\Click (Click_Standard_02).wav')

        from main import Game

        self.input_file = r'unity\Slot-Simulator-cleo_psychophys\Assets\StreamingAssets\reelData.csv'

        existing_spin_counts = self.read_existing_spin_counts(self.input_file)

        self.spincount = [i for i in range(1, 1001) if i not in existing_spin_counts]
        self.currspincount = self.spincount[0] if self.spincount else None
        
        self.images = self.load_images()
        self.selected_symbol = None
        self.drop = self.create_drop()
        self.drag = self.create_drag()

        self.payline_num_font = pygame.font.Font(r'Font\ARBLI.ttf', 20)

        self.reel1_spin_times = 5000
        self.reel2_spin_times = 5400
        self.reel3_spin_times = 5800
        self.reel4_spin_times = 6200
        self.reel5_spin_times = 6400

        self.win_amount_line_1 = 0
        self.win_amount_line_2 = 0
        self.win_amount_line_3 = 0
        self.win_amount_line_4 = 0
        self.win_amount_line_5 = 0
        self.win_amount_line_6 = 0
        self.win_amount_line_7 = 0
        self.win_amount_line_8 = 0
        self.win_amount_line_9 = 0
        self.win_amount_line_10 = 0
        self.win_amount_line_11 = 0
        self.win_amount_line_12 = 0
        self.win_amount_line_13 = 0
        self.win_amount_line_14 = 0
        self.win_amount_line_15 = 0
        self.win_amount_line_16 = 0
        self.win_amount_line_17 = 0
        self.win_amount_line_18 = 0
        self.win_amount_line_19 = 0
        self.win_amount_line_20 = 0
        self.win_amount_line_21 = 0
        self.win_amount_line_22 = 0
        self.win_amount_line_23 = 0
        self.win_amount_line_24 = 0
        self.win_amount_line_25 = 0
        self.win_amount_line_26 = 0
        self.win_amount_line_27 = 0
        self.win_amount_line_28 = 0
        self.win_amount_line_29 = 0
        self.win_amount_line_30 = 0
        self.win_amount_line_31 = 0
        self.win_amount_line_32 = 0
        self.win_amount_line_33 = 0
        self.win_amount_line_34 = 0
        self.win_amount_line_35 = 0
        self.win_amount_line_36 = 0
        self.win_amount_line_37 = 0
        self.win_amount_line_38 = 0
        self.win_amount_line_39 = 0
        self.win_amount_line_40 = 0

        
    def get_font(self, size):
        return pygame.font.Font('Font\Arial Black.ttf', size)
    
    def read_existing_spin_counts(self, file_path):
        try:
            df = pd.read_csv(file_path, header=None)
            # Check if the dataframe is empty
            if df.empty:
                print("The CSV file is empty.")
                return []
            unique_spins = df[0].unique()
            return unique_spins
        except pd.errors.EmptyDataError:
            print("The CSV file is empty or does not contain valid data.")
            return []
    
    def separator(self):
        separator_red = pygame.image.load('Sprite\separator_red.png')
        separator_red_end_left = pygame.image.load('Sprite\separator_red_end_left.png')
        separator_red_end_right = pygame.image.load('Sprite\separator_red_end_right.png')
        xseparator1, xseparator2, xseparator3, xseparator4, xseparator5, xseparator6 = ((self.display_surface.get_size()[0] / 2) - 757.5), ((self.display_surface.get_size()[0] / 2) - 450), ((self.display_surface.get_size()[0] / 2) - 150), ((self.display_surface.get_size()[0] / 2) + 150), ((self.display_surface.get_size()[0] / 2) + 450), ((self.display_surface.get_size()[0] / 2) + 762.5)
        yseparator = (self.display_surface.get_size()[1] / 2) - 55
        rectseparator1 = separator_red_end_left.get_rect(center = (xseparator1, yseparator))
        rectseparator2 = separator_red.get_rect(center = (xseparator2, yseparator))
        rectseparator3 = separator_red.get_rect(center = (xseparator3, yseparator))
        rectseparator4 = separator_red.get_rect(center = (xseparator4, yseparator))
        rectseparator5 = separator_red.get_rect(center = (xseparator5, yseparator))
        rectseparator6 = separator_red_end_right.get_rect(center = (xseparator6, yseparator))
        self.display_surface.blit(separator_red_end_right, rectseparator1)
        self.display_surface.blit(separator_red, rectseparator2)
        self.display_surface.blit(separator_red, rectseparator3)
        self.display_surface.blit(separator_red, rectseparator4)
        self.display_surface.blit(separator_red, rectseparator5)
        self.display_surface.blit(separator_red_end_left, rectseparator6)

    def frame(self):
        # FRAME
        frame_png = pygame.image.load(r'Sprite\frame.png')
        frame_scaled = pygame.transform.scale(frame_png, (1680, 1050))
        frame_rect = frame_scaled.get_rect(center = (self.display_surface.get_size()[0] / 2, self.display_surface.get_size()[1] / 2))
        self.display_surface.blit(frame_scaled, frame_rect)

    def spin_count(self):
        gauge = pygame.image.load('Sprite\circle_100.png')
        x, y = 15, self.display_surface.get_size()[1] - 25
        gauge_rect = gauge.get_rect(bottomleft = (x, y))
        self.display_surface.blit(gauge, gauge_rect)

        num_text = self.get_font(25).render(str(self.currspincount), True, "White")
        num_text_width, num_text_height = num_text.get_size()
        num_text_x = gauge_rect.centerx - num_text_width // 2
        num_text_y = (gauge_rect.centery - num_text_height // 2)
        num_text_rect = pygame.Rect(num_text_x, num_text_y, num_text_width, num_text_height)
        self.display_surface.blit(num_text, num_text_rect)

        rightplus = pygame.image.load(r'Sprite\rightplus.png')
        rightplus.set_alpha(128)
        rightplus_rect = rightplus.get_rect(bottomright = (gauge_rect.right, gauge_rect.bottom))
        self.display_surface.blit(rightplus, rightplus_rect)
        plus_text = self.get_font(15).render("+", True, "Black")
        plus_text_width, plus_text_height = plus_text.get_size()
        plus_text_x = rightplus_rect.centerx - plus_text_width // 2
        plus_text_y = (rightplus_rect.centery - plus_text_height // 2)
        plus_text_rect = pygame.Rect(plus_text_x, plus_text_y, plus_text_width, plus_text_height)
        self.display_surface.blit(plus_text, plus_text_rect)

        leftminus = pygame.image.load(r'Sprite\leftminus.png')
        leftminus.set_alpha(128)
        leftminus_rect = leftminus.get_rect(bottomleft = (gauge_rect.left, gauge_rect.bottom))
        self.display_surface.blit(leftminus, leftminus_rect)
        minus_text = self.get_font(15).render("-", True, "Black")
        minus_text_width, minus_text_height = minus_text.get_size()
        minus_text_x = leftminus_rect.centerx - minus_text_width // 2
        minus_text_y = (leftminus_rect.centery - minus_text_height // 2)
        minus_text_rect = pygame.Rect(minus_text_x, minus_text_y, minus_text_width, minus_text_height)
        self.display_surface.blit(minus_text, minus_text_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        mouse_was_pressed = False

        if mouse_click[0] and not mouse_was_pressed:
            current_index = self.spincount.index(self.currspincount)
            if leftminus_rect.collidepoint(mouse_pos):
                if current_index > 0:
                    self.currspincount = self.spincount[current_index - 1]
                self.click_sound.play()
            if rightplus_rect.collidepoint(mouse_pos):
                if current_index < len(self.spincount) - 1:
                    self.currspincount = self.spincount[current_index + 1]
                self.click_sound.play()
        
        mouse_was_pressed = mouse_click[0]

    def for_preview(self):
        keys = pygame.key.get_pressed()
        whitebg = pygame.image.load(r'Sprite\1600x900-black-solid-color-background.png')
        whitebg.set_alpha(127.5)
        whitebg_rect = whitebg.get_rect(bottomright = (self.display_surface.get_size()[0], self.display_surface.get_size()[1]))
    
        if not hasattr(self, 'show_white_bg'):
            self.show_white_bg = False
    
        if keys[pygame.K_p]:
            if not hasattr(self, 'p_key_pressed_last_frame'):
                self.p_key_pressed_last_frame = False
    
            if not self.p_key_pressed_last_frame:
                self.show_white_bg = not self.show_white_bg
                self.click_sound.play()
                self.p_key_pressed_last_frame = True
        else:
            self.p_key_pressed_last_frame = False

        if self.show_white_bg:
            self.display_surface.blit(whitebg, whitebg_rect)

    def save_input(self):
        gauge = pygame.image.load('Sprite\circle_100.png')
        x, y = self.display_surface.get_size()[0] - 115, self.display_surface.get_size()[1] - 25
        gauge_rect = gauge.get_rect(bottomleft = (x, y))
        self.display_surface.blit(gauge, gauge_rect)

        save_text = self.get_font(25).render("SAVE", True, "White")
        save_text_width, save_text_height = save_text.get_size()
        save_text_x = gauge_rect.centerx - save_text_width // 2
        save_text_y = (gauge_rect.centery - save_text_height // 2) 
        save_text_rect = pygame.Rect(save_text_x, save_text_y, save_text_width, save_text_height)
        self.display_surface.blit(save_text, save_text_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        mouse_was_pressed = False
        Balloon = pygame.image.load(r'Sprite\BG_Reel_A_halfsize.png')
        whole_rect = self.display_surface.get_rect()
        display_center = self.display_surface.get_rect().center
        Balloon_rect = Balloon.get_rect(center=display_center)

        if not hasattr(self, 'show_white_bg'):
            self.show_Balloon = False
            self.show_save_success = False

        if mouse_click[0] and not mouse_was_pressed and self.drop and all(item is not None for row in self.drop for item in row):
            if gauge_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                with open(self.input_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([self.currspincount, self.drop[0][0].replace('_300', ''), self.drop[1][0].replace('_300', ''), self.drop[2][0].replace('_300', ''), self.drop[0][1].replace('_300', ''), self.drop[1][1].replace('_300', ''), self.drop[2][1].replace('_300', ''), self.drop[0][2].replace('_300', ''), self.drop[1][2].replace('_300', ''), self.drop[2][2].replace('_300', ''), self.drop[0][3].replace('_300', ''), self.drop[1][3].replace('_300', ''), self.drop[2][3].replace('_300', ''), self.drop[0][4].replace('_300', ''), self.drop[1][4].replace('_300', ''), self.drop[2][4].replace('_300', '')])
                prevspincount = self.currspincount
                self.currspincount = self.spincount[self.spincount.index(self.currspincount) + 1]
                self.spincount.remove(prevspincount)
                self.show_save_success = True
                self.click_sound.play()
            elif whole_rect.collidepoint(mouse_pos) and self.show_save_success:
                self.show_save_success = False
                self.click_sound.play()
                self.drop[0][0] = None
                self.drop[0][1] = None
                self.drop[0][2] = None
                self.drop[0][3] = None
                self.drop[0][4] = None
                self.drop[1][0] = None
                self.drop[1][1] = None
                self.drop[1][2] = None
                self.drop[1][3] = None
                self.drop[1][4] = None
                self.drop[2][0] = None
                self.drop[2][1] = None
                self.drop[2][2] = None
                self.drop[2][3] = None
                self.drop[2][4] = None
                self.selected_symbol = None
        if self.show_save_success:
            font = pygame.font.Font('Font\Mythology-Of-Egypt.ttf', 50)
            text_lines = ["Saved successfully"]
            total_height = len(text_lines) * font.get_linesize()
            start_y = Balloon_rect.center[1] - total_height // 2 + 35

            self.display_surface.blit(Balloon, Balloon_rect)

            for i, line in enumerate(text_lines):
                text_surface = font.render(line, True, (139, 0, 0))
                text_rect = text_surface.get_rect(center=(Balloon_rect.center[0], start_y + i * font.get_linesize()))
                self.display_surface.blit(text_surface, text_rect)
        if mouse_click[0] and not mouse_was_pressed and any(None in row for row in self.drop):
            if gauge_rect.collidepoint(mouse_pos):
                self.show_Balloon = True
                self.click_sound.play()
            elif whole_rect.collidepoint(mouse_pos) and self.show_Balloon:
                self.show_Balloon = False
                self.click_sound.play()
        if self.show_Balloon:
            font = pygame.font.Font('Font\Mythology-Of-Egypt.ttf', 65)
            text_lines = ["Cannot save", "until all slots", "are filled"]
            total_height = len(text_lines) * font.get_linesize()
            start_y = Balloon_rect.center[1] - total_height // 2 + 35

            self.display_surface.blit(Balloon, Balloon_rect)

            for i, line in enumerate(text_lines):
                text_surface = font.render(line, True, (139, 0, 0))
                text_rect = text_surface.get_rect(center=(Balloon_rect.center[0], start_y + i * font.get_linesize()))
                self.display_surface.blit(text_surface, text_rect)

        mouse_was_pressed = mouse_click[0]

    def load_images(self):
        symbols = ['A_100', 'Ankh_100', 'J_100', 'K_100', 'Mask_100', 'Q_100', 'Scarab_100', 'Sfnx_100', 'Wild_100', 'Stone_100', 'Gem_100', 'Gem_300', 'A_300', 'Ankh_300', 'J_300', 'K_300', 'Mask_300', 'Q_300', 'Scarab_300', 'Sfnx_300', 'Wild_300', 'Stone_300']
        self.images = {}
        for symbol in symbols:
            self.images[symbol] = pygame.image.load(f'Sprite/Symbol/{symbol}.png')
        return self.images
    
    def create_drop_surf(self):
        drop_surf = pygame.Surface((300 * 5, 300 * 3), pygame.SRCALPHA)
        drop_surf.fill((0, 0, 0, 0))
        for y in range(3):
            for x in range(5):
                rect = pygame.Rect(x * 300, y * 300, 300, 300)
                pygame.draw.rect(drop_surf, (255, 255, 255, 0), rect, 1)
        
        return drop_surf
    
    def create_drop(self):
        drop = []
        for y in range(3):
            drop.append([])
            for x in range(5):
                drop[y].append(None)
        return drop
    
    def create_drag_surf(self):
        drag_surf = pygame.Surface((120 * 11, 120 * 1), pygame.SRCALPHA)
        drag_surf.fill((0, 0, 0, 0))
        for y in range(1):
            for x in range(11):
                rect = pygame.Rect(x * 120, y * 120, 120, 120)
                pygame.draw.rect(drag_surf, (0, 0, 255), rect, 1)

        return drag_surf
    
    def create_drag(self):
        drag = []
        for y in range(1):
            drag.append([])
            for x in range(11):
                drag[y].append(None)

        drag[0][0] = 'A_100'
        drag[0][1] = 'Ankh_100'
        drag[0][2] = 'J_100'
        drag[0][3] = 'K_100'
        drag[0][4] = 'Mask_100'
        drag[0][5] = 'Q_100'
        drag[0][6] = 'Scarab_100'
        drag[0][7] = 'Sfnx_100'
        drag[0][8] = 'Gem_100'
        drag[0][9] = 'Wild_100'
        drag[0][10] = 'Stone_100'

        return drag
    
    def get_square_under_mouse(self, drop, drag):
        drop_surf = self.create_drop_surf()
        drag_surf = self.create_drag_surf()
        
        drop_pos = ((1680 - drop_surf.get_width()) // 2, ((1050 - drop_surf.get_height()) // 2) - 55)
        drag_pos = ((self.display_surface.get_size()[0] - 1325) / 2, self.display_surface.get_size()[1] - 125)
        
        mouse_pos_drop = pygame.Vector2(pygame.mouse.get_pos()) - drop_pos
        mouse_pos_drag = pygame.Vector2(pygame.mouse.get_pos()) - drag_pos
        
        x_drop, y_drop = [int(v // 300) for i, v in enumerate(mouse_pos_drop)]
        x_drag, y_drag = [int(v // 120) for i, v in enumerate(mouse_pos_drag)]  # Assuming 120 is the size for drag
        
        try:
            if 0 <= x_drop < len(drop[0]) and 0 <= y_drop < len(drop):
                return (drop[y_drop][x_drop], x_drop, y_drop, 'drop')
            elif 0 <= x_drag < len(drag[0]) and 0 <= y_drag < len(drag):
                return (drag[y_drag][x_drag], x_drag, y_drag, 'drag')
        except IndexError: pass
        return None, None, None, None
    
    def draw_drop_pieces(self, screen, drop, drop_surf):
        # Loop through each row in the drop area
        for y in range(len(drop)):
            # Loop through each column in the current row
            for x in range(len(drop[y])):
                # Get the symbol at the current position
                symbol = drop[y][x]
                # If there is a symbol at the current position
                if symbol:
                    # Calculate the position to draw the symbol
                    pos = pygame.Rect((1680 - drop_surf.get_width()) // 2 + x * 300, ((1050 - drop_surf.get_height()) // 2) - 55 + y * 300, 300, 300)
                    # Draw the symbol on the screen at the calculated position
                    screen.blit(self.images[symbol], self.images[symbol].get_rect(center=pos.center))

    def draw_drag_pieces(self, screen, drag):
        # Loop through each row in the drag area
        for y in range(len(drag)):
            # Loop through each column in the current row
            for x in range(len(drag[y])):
                # Get the symbol at the current position
                symbol = drag[y][x]
                # If there is a symbol at the current position
                if symbol:
                    # Calculate the position to draw the symbol
                    pos = pygame.Rect((self.display_surface.get_size()[0] - 1325) / 2 + x * 120, self.display_surface.get_size()[1] - 125 + y * 120, 120, 120)
                    # Draw the symbol on the screen at the calculated position
                    screen.blit(self.images[symbol], self.images[symbol].get_rect(center=pos.center))


    def draw_selector(self, screen, symbol, x, y):
        if symbol != None:
            rect = (self.display_surface.get_size()[0] - 1325) / 2 + x * 120, self.display_surface.get_size()[1] - 125 + y * 120, 120, 120
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)
        
    def template(self):
        full_symbol_png = pygame.image.load('Sprite\Icon_Line_Stone_Resize.png')
        full_symbol_reversed_png = pygame.image.load('Sprite\Icon_Line_Stone_Reversed_Resize.png')
        TEXT_COLOR = (255, 255, 255)

        xleft, xright = ((self.display_surface.get_size()[0] / 2) - 751.5), ((self.display_surface.get_size()[0] / 2) + 760)
        y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20 = 130, 166.75, 203.5, 240.25, 277, 313.75, 350.5, 387.25, 424, 460.75, 497.5, 534.25, 571, 607.75, 644.5, 681.25, 718, 754.75, 791.5, 828.25

        symbol1_rect = full_symbol_png.get_rect(bottomright = (xleft, y1))
        symbol2_rect = full_symbol_png.get_rect(bottomright = (xleft, y2))
        symbol3_rect = full_symbol_png.get_rect(bottomright = (xleft, y3))
        symbol4_rect = full_symbol_png.get_rect(bottomright = (xleft, y4))
        symbol5_rect = full_symbol_png.get_rect(bottomright = (xleft, y5))
        symbol6_rect = full_symbol_png.get_rect(bottomright = (xleft, y6))
        symbol7_rect = full_symbol_png.get_rect(bottomright = (xleft, y7))
        symbol8_rect = full_symbol_png.get_rect(bottomright = (xleft, y8))
        symbol9_rect = full_symbol_png.get_rect(bottomright = (xleft, y9))
        symbol10_rect = full_symbol_png.get_rect(bottomright = (xleft, y10))
        symbol11_rect = full_symbol_png.get_rect(bottomright = (xleft, y11))
        symbol12_rect = full_symbol_png.get_rect(bottomright = (xleft, y12))
        symbol13_rect = full_symbol_png.get_rect(bottomright = (xleft, y13))
        symbol14_rect = full_symbol_png.get_rect(bottomright = (xleft, y14))
        symbol15_rect = full_symbol_png.get_rect(bottomright = (xleft, y15))
        symbol16_rect = full_symbol_png.get_rect(bottomright = (xleft, y16))
        symbol17_rect = full_symbol_png.get_rect(bottomright = (xleft, y17))
        symbol18_rect = full_symbol_png.get_rect(bottomright = (xleft, y18))
        symbol19_rect = full_symbol_png.get_rect(bottomright = (xleft, y19))
        symbol20_rect = full_symbol_png.get_rect(bottomright = (xleft, y20))
        
        symbol21_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y1))
        symbol22_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y2))
        symbol23_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y3))
        symbol24_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y4))
        symbol25_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y5))
        symbol26_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y6))
        symbol27_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y7))
        symbol28_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y8))
        symbol29_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y9))
        symbol30_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y10))
        symbol31_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y11))
        symbol32_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y12))
        symbol33_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y13))
        symbol34_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y14))
        symbol35_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y15))
        symbol36_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y16))
        symbol37_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y17))
        symbol38_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y18))
        symbol39_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y19))
        symbol40_rect = full_symbol_reversed_png.get_rect(bottomleft = (xright, y20))

        full_paylines_1_txt = self.payline_num_font.render("1", True, (255, 221, 178), None)
        full_paylines_2_txt = self.payline_num_font.render("2", True, (255, 221, 178), None)
        full_paylines_3_txt = self.payline_num_font.render("3", True, (255, 221, 178), None)
        full_paylines_4_txt = self.payline_num_font.render("4", True, (255, 221, 178), None)
        full_paylines_5_txt = self.payline_num_font.render("5", True, (255, 221, 178), None)
        full_paylines_6_txt = self.payline_num_font.render("6", True, (255, 221, 178), None)
        full_paylines_7_txt = self.payline_num_font.render("7", True, (255, 221, 178), None)
        full_paylines_8_txt = self.payline_num_font.render("8", True, (255, 221, 178), None)
        full_paylines_9_txt = self.payline_num_font.render("9", True, (255, 221, 178), None)
        full_paylines_10_txt = self.payline_num_font.render("10", True, (255, 221, 178), None)
        full_paylines_11_txt = self.payline_num_font.render("11", True, (255, 221, 178), None)
        full_paylines_12_txt = self.payline_num_font.render("12", True, (255, 221, 178), None)
        full_paylines_13_txt = self.payline_num_font.render("13", True, (255, 221, 178), None)
        full_paylines_14_txt = self.payline_num_font.render("14", True, (255, 221, 178), None)
        full_paylines_15_txt = self.payline_num_font.render("15", True, (255, 221, 178), None)
        full_paylines_16_txt = self.payline_num_font.render("16", True, (255, 221, 178), None)
        full_paylines_17_txt = self.payline_num_font.render("17", True, (255, 221, 178), None)
        full_paylines_18_txt = self.payline_num_font.render("18", True, (255, 221, 178), None)
        full_paylines_19_txt = self.payline_num_font.render("19", True, (255, 221, 178), None)
        full_paylines_20_txt = self.payline_num_font.render("20", True, (255, 221, 178), None)
        full_paylines_21_txt = self.payline_num_font.render("21", True, (255, 221, 178), None)
        full_paylines_22_txt = self.payline_num_font.render("22", True, (255, 221, 178), None)
        full_paylines_23_txt = self.payline_num_font.render("23", True, (255, 221, 178), None)
        full_paylines_24_txt = self.payline_num_font.render("24", True, (255, 221, 178), None)
        full_paylines_25_txt = self.payline_num_font.render("25", True, (255, 221, 178), None)
        full_paylines_26_txt = self.payline_num_font.render("26", True, (255, 221, 178), None)
        full_paylines_27_txt = self.payline_num_font.render("27", True, (255, 221, 178), None)
        full_paylines_28_txt = self.payline_num_font.render("28", True, (255, 221, 178), None)
        full_paylines_29_txt = self.payline_num_font.render("29", True, (255, 221, 178), None)
        full_paylines_30_txt = self.payline_num_font.render("30", True, (255, 221, 178), None)
        full_paylines_31_txt = self.payline_num_font.render("31", True, (255, 221, 178), None)
        full_paylines_32_txt = self.payline_num_font.render("32", True, (255, 221, 178), None)
        full_paylines_33_txt = self.payline_num_font.render("33", True, (255, 221, 178), None)
        full_paylines_34_txt = self.payline_num_font.render("34", True, (255, 221, 178), None)
        full_paylines_35_txt = self.payline_num_font.render("35", True, (255, 221, 178), None)
        full_paylines_36_txt = self.payline_num_font.render("36", True, (255, 221, 178), None)
        full_paylines_37_txt = self.payline_num_font.render("37", True, (255, 221, 178), None)
        full_paylines_38_txt = self.payline_num_font.render("38", True, (255, 221, 178), None)
        full_paylines_39_txt = self.payline_num_font.render("39", True, (255, 221, 178), None)
        full_paylines_40_txt = self.payline_num_font.render("40", True, (255, 221, 178), None)

        paylines_1_txt_rect = full_paylines_1_txt.get_rect(center=(symbol1_rect.centerx - 3.5, symbol1_rect.centery - 1.5))
        paylines_2_txt_rect = full_paylines_2_txt.get_rect(center=(symbol2_rect.centerx - 3.5, symbol2_rect.centery - 1.5))
        paylines_3_txt_rect = full_paylines_3_txt.get_rect(center=(symbol3_rect.centerx - 3.5, symbol3_rect.centery - 1.5))
        paylines_4_txt_rect = full_paylines_4_txt.get_rect(center=(symbol4_rect.centerx - 3.5, symbol4_rect.centery - 1.5))
        paylines_5_txt_rect = full_paylines_5_txt.get_rect(center=(symbol5_rect.centerx - 3.5, symbol5_rect.centery - 1.5))
        paylines_6_txt_rect = full_paylines_6_txt.get_rect(center=(symbol6_rect.centerx - 3.5, symbol6_rect.centery - 1.5))
        paylines_7_txt_rect = full_paylines_7_txt.get_rect(center=(symbol7_rect.centerx - 3.5, symbol7_rect.centery - 1.5))
        paylines_8_txt_rect = full_paylines_8_txt.get_rect(center=(symbol8_rect.centerx - 3.5, symbol8_rect.centery - 1.5))
        paylines_9_txt_rect = full_paylines_9_txt.get_rect(center=(symbol9_rect.centerx - 3.5, symbol9_rect.centery - 1.5))
        paylines_10_txt_rect = full_paylines_10_txt.get_rect(center=(symbol10_rect.centerx - 3.5, symbol10_rect.centery - 1.5))
        paylines_11_txt_rect = full_paylines_11_txt.get_rect(center=(symbol11_rect.centerx - 3.5, symbol11_rect.centery - 1.5))
        paylines_12_txt_rect = full_paylines_12_txt.get_rect(center=(symbol12_rect.centerx - 3.5, symbol12_rect.centery - 1.5))
        paylines_13_txt_rect = full_paylines_13_txt.get_rect(center=(symbol13_rect.centerx - 3.5, symbol13_rect.centery - 1.5))
        paylines_14_txt_rect = full_paylines_14_txt.get_rect(center=(symbol14_rect.centerx - 3.5, symbol14_rect.centery - 1.5))
        paylines_15_txt_rect = full_paylines_15_txt.get_rect(center=(symbol15_rect.centerx - 3.5, symbol15_rect.centery - 1.5))
        paylines_16_txt_rect = full_paylines_16_txt.get_rect(center=(symbol16_rect.centerx - 3.5, symbol16_rect.centery - 1.5))
        paylines_17_txt_rect = full_paylines_17_txt.get_rect(center=(symbol17_rect.centerx - 3.5, symbol17_rect.centery - 1.5))
        paylines_18_txt_rect = full_paylines_18_txt.get_rect(center=(symbol18_rect.centerx - 3.5, symbol18_rect.centery - 1.5))
        paylines_19_txt_rect = full_paylines_19_txt.get_rect(center=(symbol19_rect.centerx - 3.5, symbol19_rect.centery - 1.5))
        paylines_20_txt_rect = full_paylines_20_txt.get_rect(center=(symbol20_rect.centerx - 3.5, symbol20_rect.centery - 1.5))
        paylines_21_txt_rect = full_paylines_21_txt.get_rect(center=(symbol21_rect.centerx, symbol21_rect.centery - 1.5))
        paylines_22_txt_rect = full_paylines_22_txt.get_rect(center=(symbol22_rect.centerx, symbol22_rect.centery - 1.5))
        paylines_23_txt_rect = full_paylines_23_txt.get_rect(center=(symbol23_rect.centerx, symbol23_rect.centery - 1.5))
        paylines_24_txt_rect = full_paylines_24_txt.get_rect(center=(symbol24_rect.centerx, symbol24_rect.centery - 1.5))
        paylines_25_txt_rect = full_paylines_25_txt.get_rect(center=(symbol25_rect.centerx, symbol25_rect.centery - 1.5))
        paylines_26_txt_rect = full_paylines_26_txt.get_rect(center=(symbol26_rect.centerx, symbol26_rect.centery - 1.5))
        paylines_27_txt_rect = full_paylines_27_txt.get_rect(center=(symbol27_rect.centerx, symbol27_rect.centery - 1.5))
        paylines_28_txt_rect = full_paylines_28_txt.get_rect(center=(symbol28_rect.centerx, symbol28_rect.centery - 1.5))
        paylines_29_txt_rect = full_paylines_29_txt.get_rect(center=(symbol29_rect.centerx, symbol29_rect.centery - 1.5))
        paylines_30_txt_rect = full_paylines_30_txt.get_rect(center=(symbol30_rect.centerx, symbol30_rect.centery - 1.5))
        paylines_31_txt_rect = full_paylines_31_txt.get_rect(center=(symbol31_rect.centerx, symbol31_rect.centery - 1.5))
        paylines_32_txt_rect = full_paylines_32_txt.get_rect(center=(symbol32_rect.centerx, symbol32_rect.centery - 1.5))
        paylines_33_txt_rect = full_paylines_33_txt.get_rect(center=(symbol33_rect.centerx, symbol33_rect.centery - 1.5))
        paylines_34_txt_rect = full_paylines_34_txt.get_rect(center=(symbol34_rect.centerx, symbol34_rect.centery - 1.5))
        paylines_35_txt_rect = full_paylines_35_txt.get_rect(center=(symbol35_rect.centerx, symbol35_rect.centery - 1.5))
        paylines_36_txt_rect = full_paylines_36_txt.get_rect(center=(symbol36_rect.centerx, symbol36_rect.centery - 1.5))
        paylines_37_txt_rect = full_paylines_37_txt.get_rect(center=(symbol37_rect.centerx, symbol37_rect.centery - 1.5))
        paylines_38_txt_rect = full_paylines_38_txt.get_rect(center=(symbol38_rect.centerx, symbol38_rect.centery - 1.5))
        paylines_39_txt_rect = full_paylines_39_txt.get_rect(center=(symbol39_rect.centerx, symbol39_rect.centery - 1.5))
        paylines_40_txt_rect = full_paylines_40_txt.get_rect(center=(symbol40_rect.centerx, symbol40_rect.centery - 1.5))

        self.display_surface.blit(full_symbol_png, symbol1_rect)
        self.display_surface.blit(full_paylines_1_txt, paylines_1_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol2_rect)
        self.display_surface.blit(full_paylines_2_txt, paylines_2_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol3_rect)
        self.display_surface.blit(full_paylines_3_txt, paylines_3_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol4_rect)
        self.display_surface.blit(full_paylines_4_txt, paylines_4_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol5_rect)
        self.display_surface.blit(full_paylines_5_txt, paylines_5_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol6_rect)
        self.display_surface.blit(full_paylines_6_txt, paylines_6_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol7_rect)
        self.display_surface.blit(full_paylines_7_txt, paylines_7_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol8_rect)
        self.display_surface.blit(full_paylines_8_txt, paylines_8_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol9_rect)
        self.display_surface.blit(full_paylines_9_txt, paylines_9_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol10_rect)
        self.display_surface.blit(full_paylines_10_txt, paylines_10_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol11_rect)
        self.display_surface.blit(full_paylines_11_txt, paylines_11_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol12_rect)
        self.display_surface.blit(full_paylines_12_txt, paylines_12_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol13_rect)
        self.display_surface.blit(full_paylines_13_txt, paylines_13_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol14_rect)
        self.display_surface.blit(full_paylines_14_txt, paylines_14_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol15_rect)
        self.display_surface.blit(full_paylines_15_txt, paylines_15_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol16_rect)
        self.display_surface.blit(full_paylines_16_txt, paylines_16_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol17_rect)
        self.display_surface.blit(full_paylines_17_txt, paylines_17_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol18_rect)
        self.display_surface.blit(full_paylines_18_txt, paylines_18_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol19_rect)
        self.display_surface.blit(full_paylines_19_txt, paylines_19_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol20_rect)
        self.display_surface.blit(full_paylines_20_txt, paylines_20_txt_rect)
        self.display_surface.blit(full_symbol_png, symbol21_rect)
        self.display_surface.blit(full_paylines_21_txt, paylines_21_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol22_rect)
        self.display_surface.blit(full_paylines_22_txt, paylines_22_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol23_rect)
        self.display_surface.blit(full_paylines_23_txt, paylines_23_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol24_rect)
        self.display_surface.blit(full_paylines_24_txt, paylines_24_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol25_rect)
        self.display_surface.blit(full_paylines_25_txt, paylines_25_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol26_rect)
        self.display_surface.blit(full_paylines_26_txt, paylines_26_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol27_rect)
        self.display_surface.blit(full_paylines_27_txt, paylines_27_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol28_rect)
        self.display_surface.blit(full_paylines_28_txt, paylines_28_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol29_rect)
        self.display_surface.blit(full_paylines_29_txt, paylines_29_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol30_rect)
        self.display_surface.blit(full_paylines_30_txt, paylines_30_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol31_rect)
        self.display_surface.blit(full_paylines_31_txt, paylines_31_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol32_rect)
        self.display_surface.blit(full_paylines_32_txt, paylines_32_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol33_rect)
        self.display_surface.blit(full_paylines_33_txt, paylines_33_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol34_rect)
        self.display_surface.blit(full_paylines_34_txt, paylines_34_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol35_rect)
        self.display_surface.blit(full_paylines_35_txt, paylines_35_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol36_rect)
        self.display_surface.blit(full_paylines_36_txt, paylines_36_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol37_rect)
        self.display_surface.blit(full_paylines_37_txt, paylines_37_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol38_rect)
        self.display_surface.blit(full_paylines_38_txt, paylines_38_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol39_rect)
        self.display_surface.blit(full_paylines_39_txt, paylines_39_txt_rect)
        self.display_surface.blit(full_symbol_reversed_png, symbol40_rect)
        self.display_surface.blit(full_paylines_40_txt, paylines_40_txt_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        mouse_was_pressed = False
        symbols = ['A_300', 'Ankh_300', 'J_300', 'K_300', 'Mask_300', 'Q_300', 'Scarab_300', 'Sfnx_300', 'Wild_300', 'Stone_300', 'Gem_300']

        if mouse_click[0] and not mouse_was_pressed:
            if symbol1_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = symbol_output
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol2_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = symbol_output
                self.drop[0][2] = symbol_output
                self.drop[0][3] = symbol_output
                self.drop[0][4] = symbol_output
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol3_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = symbol_output
                self.drop[2][1] = symbol_output
                self.drop[2][2] = symbol_output
                self.drop[2][3] = symbol_output
                self.drop[2][4] = symbol_output
            if symbol4_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = symbol_output
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = symbol_output
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol5_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = symbol_output
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = symbol_output
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = symbol_output
            if symbol6_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = symbol_output
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = symbol_output
                self.drop[2][4] = random.choice(symbols)
            if symbol7_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = symbol_output
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = symbol_output
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol8_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = symbol_output
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = symbol_output
                self.drop[2][4] = symbol_output
            if symbol9_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = symbol_output
                self.drop[0][4] = symbol_output
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = symbol_output
                self.drop[2][1] = symbol_output
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol10_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = symbol_output
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = symbol_output
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol11_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = symbol_output
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = symbol_output
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = symbol_output
            if symbol12_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = symbol_output
                self.drop[0][2] = symbol_output
                self.drop[0][3] = symbol_output
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol13_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = symbol_output
                self.drop[2][2] = symbol_output
                self.drop[2][3] = symbol_output
                self.drop[2][4] = random.choice(symbols)
            if symbol14_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = symbol_output
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol15_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = symbol_output
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = symbol_output
            if symbol16_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = symbol_output
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol17_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = symbol_output
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol18_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = symbol_output
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = symbol_output
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol19_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = symbol_output
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = symbol_output
                self.drop[2][4] = random.choice(symbols)
            if symbol20_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = symbol_output
                self.drop[0][2] = symbol_output
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = symbol_output
            if symbol21_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = symbol_output
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = symbol_output
                self.drop[2][1] = symbol_output
                self.drop[2][2] = symbol_output
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol22_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = symbol_output
                self.drop[2][3] = symbol_output
                self.drop[2][4] = symbol_output
            if symbol23_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = symbol_output
                self.drop[0][3] = symbol_output
                self.drop[0][4] = symbol_output
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = symbol_output
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol24_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = symbol_output
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol25_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = symbol_output
                self.drop[2][4] = random.choice(symbols)
            if symbol26_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = symbol_output
            if symbol27_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = symbol_output
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = symbol_output
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol28_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = symbol_output
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = symbol_output
                self.drop[2][1] = symbol_output
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol29_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = symbol_output
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = symbol_output
                self.drop[2][4] = random.choice(symbols)
            if symbol30_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = symbol_output
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = symbol_output
                self.drop[2][3] = symbol_output
                self.drop[2][4] = symbol_output
            if symbol31_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = symbol_output
                self.drop[0][3] = symbol_output
                self.drop[0][4] = symbol_output
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol32_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = symbol_output
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol33_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = symbol_output
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = symbol_output
                self.drop[1][4] = symbol_output
                self.drop[2][0] = symbol_output
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol34_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = symbol_output
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = symbol_output
                self.drop[0][4] = symbol_output
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol35_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = symbol_output
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = symbol_output
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = symbol_output
                self.drop[2][4] = symbol_output
            if symbol36_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = symbol_output
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = symbol_output
                self.drop[1][4] = symbol_output
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol37_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = random.choice(symbols)
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = symbol_output
                self.drop[1][4] = symbol_output
                self.drop[2][0] = symbol_output
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol38_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = symbol_output
                self.drop[0][2] = symbol_output
                self.drop[0][3] = symbol_output
                self.drop[0][4] = symbol_output
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)
            if symbol39_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = random.choice(symbols)
                self.drop[1][0] = symbol_output
                self.drop[1][1] = random.choice(symbols)
                self.drop[1][2] = random.choice(symbols)
                self.drop[1][3] = random.choice(symbols)
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = symbol_output
                self.drop[2][2] = symbol_output
                self.drop[2][3] = symbol_output
                self.drop[2][4] = symbol_output
            if symbol40_rect.collidepoint(mouse_pos):
                self.click_sound.play()
                symbol_output = random.choice(symbols)
                self.drop[0][0] = random.choice(symbols)
                self.drop[0][1] = random.choice(symbols)
                self.drop[0][2] = random.choice(symbols)
                self.drop[0][3] = random.choice(symbols)
                self.drop[0][4] = symbol_output
                self.drop[1][0] = symbol_output
                self.drop[1][1] = symbol_output
                self.drop[1][2] = symbol_output
                self.drop[1][3] = symbol_output
                self.drop[1][4] = random.choice(symbols)
                self.drop[2][0] = random.choice(symbols)
                self.drop[2][1] = random.choice(symbols)
                self.drop[2][2] = random.choice(symbols)
                self.drop[2][3] = random.choice(symbols)
                self.drop[2][4] = random.choice(symbols)

    def check_5_symbols(self, line_attr, symbols):
        # Get the current line value
        line_value = 0

        if symbols == 'A_300':
            line_value = 50
        elif symbols == 'Ankh_300':
            line_value = 100
        elif symbols == 'J_300':
            line_value = 50
        elif symbols == 'K_300':
            line_value = 75
        elif symbols == 'Q_300':
            line_value = 75
        elif symbols == 'Scarab_300':
            line_value = 200
        elif symbols == 'Sfnx_300':
            line_value = 1000
        elif symbols == 'Stone_300':
            line_value = 100
        elif symbols == 'Gem_300':
            line_value = 500
        elif symbols == 'Wild_300':
            line_value = 1000

        # Set the value to the desired line
        setattr(self, line_attr, line_value)

    def check_4_symbols(self, line_attr, symbols):
        # Get the current line value
        line_value = 0

        if symbols == 'A_300':
            line_value = 15
        elif symbols == 'Ankh_300':
            line_value = 30
        elif symbols == 'J_300':
            line_value = 15
        elif symbols == 'K_300':
            line_value = 20
        elif symbols == 'Q_300':
            line_value = 20
        elif symbols == 'Scarab_300':
            line_value = 100
        elif symbols == 'Sfnx_300':
            line_value = 100
        elif symbols == 'Stone_300':
            line_value = 30
        elif symbols == 'Gem_300':
            line_value = 200

        # Set the value to the desired line
        setattr(self, line_attr, line_value)

    def check_3_symbols(self, line_attr, symbols):
        # Get the current line value
        line_value = 0
    
        if symbols == 'A_300':
            line_value = 5
        elif symbols == 'Ankh_300':
            line_value = 10
        elif symbols == 'J_300':
            line_value = 5
        elif symbols == 'K_300':
            line_value = 5
        elif symbols == 'Q_300':
            line_value = 5
        elif symbols == 'Scarab_300':
            line_value = 40
        elif symbols == 'Sfnx_300':
            line_value = 40
        elif symbols == 'Stone_300':
            line_value = 10
        elif symbols == 'Gem_300':
            line_value = 50

        # Set the value to the desired line
        setattr(self, line_attr, line_value)


    def win_amount_display(self):
        self.win_amount_total = self.win_amount_line_1 + self.win_amount_line_2 + self.win_amount_line_3 + self.win_amount_line_4 + self.win_amount_line_5 + self.win_amount_line_6 + self.win_amount_line_7 + self.win_amount_line_8 + self.win_amount_line_9 + self.win_amount_line_10 + self.win_amount_line_11 + self.win_amount_line_12 + self.win_amount_line_13 + self.win_amount_line_14 + self.win_amount_line_15 + self.win_amount_line_16 + self.win_amount_line_17 + self.win_amount_line_18 + self.win_amount_line_19 + self.win_amount_line_20 + self.win_amount_line_21 + self.win_amount_line_22 + self.win_amount_line_23 + self.win_amount_line_24 + self.win_amount_line_25 + self.win_amount_line_26 + self.win_amount_line_27 + self.win_amount_line_28 + self.win_amount_line_29 + self.win_amount_line_30 + self.win_amount_line_31 + self.win_amount_line_32 + self.win_amount_line_33 + self.win_amount_line_34 + self.win_amount_line_35 + self.win_amount_line_36 + self.win_amount_line_37 + self.win_amount_line_38 + self.win_amount_line_39 + self.win_amount_line_40
        gauge = pygame.image.load(r'Sprite\smallgauge.png')
        x, y = self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] - 175
        gauge_rect = gauge.get_rect(center=(x, y))
        self.display_surface.blit(gauge, gauge_rect)

        num_text = self.get_font(25).render(f'{self.win_amount_total}', True, "White")
        num_text_rect = num_text.get_rect(center=(x, y))
        self.display_surface.blit(num_text, num_text_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        mouse_was_clicked = False

        if gauge_rect.collidepoint(mouse_pos) and mouse_click[0] and not mouse_was_clicked:
            self.win_amount_line_1 = 0
            self.check_win_amt_line_1()
            self.win_amount_line_2 = 0
            self.check_win_amt_line_2()
            self.win_amount_line_3 = 0
            self.check_win_amt_line_3()
            self.win_amount_line_4 = 0
            self.check_win_amt_line_4()
            self.win_amount_line_5 = 0
            self.check_win_amt_line_5()
            self.win_amount_line_6 = 0
            self.check_win_amt_line_6()
            self.win_amount_line_7 = 0
            self.check_win_amt_line_7()
            self.win_amount_line_8 = 0
            self.check_win_amt_line_8()
            self.win_amount_line_9 = 0
            self.check_win_amt_line_9()
            self.win_amount_line_10 = 0
            self.check_win_amt_line_10()
            self.win_amount_line_11 = 0
            self.check_win_amt_line_11()
            self.win_amount_line_12 = 0
            self.check_win_amt_line_12()
            self.win_amount_line_13 = 0
            self.check_win_amt_line_13()
            self.win_amount_line_14 = 0
            self.check_win_amt_line_14()
            self.win_amount_line_15 = 0
            self.check_win_amt_line_15()
            self.win_amount_line_16 = 0
            self.check_win_amt_line_16()
            self.win_amount_line_17 = 0
            self.check_win_amt_line_17()
            self.win_amount_line_18 = 0
            self.check_win_amt_line_18()
            self.win_amount_line_19 = 0
            self.check_win_amt_line_19()
            self.win_amount_line_20 = 0
            self.check_win_amt_line_20()
            self.win_amount_line_21 = 0
            self.check_win_amt_line_21()
            self.win_amount_line_22 = 0
            self.check_win_amt_line_22()
            self.win_amount_line_23 = 0
            self.check_win_amt_line_23()
            self.win_amount_line_24 = 0
            self.check_win_amt_line_24()
            self.win_amount_line_25 = 0
            self.check_win_amt_line_25()
            self.win_amount_line_26 = 0
            self.check_win_amt_line_26()
            self.win_amount_line_27 = 0
            self.check_win_amt_line_27()
            self.win_amount_line_28 = 0
            self.check_win_amt_line_28()
            self.win_amount_line_29 = 0
            self.check_win_amt_line_29()
            self.win_amount_line_30 = 0
            self.check_win_amt_line_30()
            self.win_amount_line_31 = 0
            self.check_win_amt_line_31()
            self.win_amount_line_32 = 0
            self.check_win_amt_line_32()
            self.win_amount_line_33 = 0
            self.check_win_amt_line_33()
            self.win_amount_line_34 = 0
            self.check_win_amt_line_34()
            self.win_amount_line_35 = 0
            self.check_win_amt_line_35()
            self.win_amount_line_36 = 0
            self.check_win_amt_line_36()
            self.win_amount_line_37 = 0
            self.check_win_amt_line_37()
            self.win_amount_line_38 = 0
            self.check_win_amt_line_38()
            self.win_amount_line_39 = 0
            self.check_win_amt_line_39()
            self.win_amount_line_40 = 0
            self.check_win_amt_line_40()
        
        mouse_was_clicked = mouse_click[0]

    def is_match(self, symbol1, symbol2):
        return symbol1 == symbol2 or symbol1 == 'Wild_300' or symbol2 == 'Wild_300'
    
    def check_win_amt_line_1(self):
        if self.is_match(self.drop[1][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_1", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_1", self.drop[1][3])
                if self.is_match(self.drop[1][3], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_1", self.drop[1][4])
    
    def check_win_amt_line_2(self):
        if self.is_match(self.drop[0][0], self.drop[0][1]) and self.is_match(self.drop[0][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_2", self.drop[0][2])
            if self.is_match(self.drop[0][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_2", self.drop[0][3])
                if self.is_match(self.drop[0][3], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_2", self.drop[0][4])
    
    def check_win_amt_line_3(self):
        if self.is_match(self.drop[2][0], self.drop[2][1]) and self.is_match(self.drop[2][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_3", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_3", self.drop[2][3])
                if self.is_match(self.drop[2][3], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_3", self.drop[2][4])
    
    def check_win_amt_line_4(self):
        if self.is_match(self.drop[0][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_4", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_4", self.drop[1][3])
                if self.is_match(self.drop[1][3], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_4", self.drop[0][4])
    
    def check_win_amt_line_5(self):
        if self.is_match(self.drop[2][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_5", self.drop[0][2])
            if self.is_match(self.drop[0][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_5", self.drop[1][3])
                if self.is_match(self.drop[1][3], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_5", self.drop[2][4])

    def check_win_amt_line_6(self):
        if self.is_match(self.drop[1][0], self.drop[0][1]) and self.is_match(self.drop[0][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_6", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_6", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_6", self.drop[1][2])

    def check_win_amt_line_7(self):
        if self.is_match(self.drop[1][0], self.drop[2][1]) and self.is_match(self.drop[2][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_7", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_7", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_7", self.drop[1][2])

    def check_win_amt_line_8(self):
        if self.is_match(self.drop[0][0], self.drop[0][1]) and self.is_match(self.drop[0][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_8", self.drop[0][2])
            if self.is_match(self.drop[1][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_8", self.drop[0][2])
                if self.is_match(self.drop[1][2], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_8", self.drop[0][2])

    def check_win_amt_line_9(self):
        if self.is_match(self.drop[2][0], self.drop[2][1]) and self.is_match(self.drop[2][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_9", self.drop[2][2])
            if self.is_match(self.drop[1][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_9", self.drop[2][2])
                if self.is_match(self.drop[1][2], self.drop[0][4]):
                        self.check_5_symbols("win_amount_line_9", self.drop[2][2])

    def check_win_amt_line_10(self):
        if self.is_match(self.drop[0][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_10", self.drop[0][2])
            if self.is_match(self.drop[0][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_10", self.drop[0][2])
                if self.is_match(self.drop[0][2], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_10", self.drop[0][2])

    def check_win_amt_line_11(self):
        if self.is_match(self.drop[2][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_11", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_11", self.drop[2][2])
                if self.is_match(self.drop[2][2], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_11", self.drop[2][2])

    def check_win_amt_line_12(self):
        if self.is_match(self.drop[1][0], self.drop[0][1]) and self.is_match(self.drop[0][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_12", self.drop[0][2])
            if self.is_match(self.drop[0][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_12", self.drop[0][2])
                if self.is_match(self.drop[0][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_12", self.drop[0][2])

    def check_win_amt_line_13(self):
        if self.is_match(self.drop[1][0], self.drop[2][1]) and self.is_match(self.drop[2][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_13", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_13", self.drop[2][2])
                if self.is_match(self.drop[2][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_13", self.drop[2][2])

    def check_win_amt_line_14(self):
        if self.is_match(self.drop[0][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_14", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_14", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_14", self.drop[1][2])

    def check_win_amt_line_15(self):
        if self.is_match(self.drop[2][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_15", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_15", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_15", self.drop[1][2])

    def check_win_amt_line_16(self):
        if self.is_match(self.drop[1][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_16", self.drop[1][2])
            if self.is_match(self.drop[0][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_16", self.drop[1][2])
                if self.is_match(self.drop[0][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_16", self.drop[1][2])

    def check_win_amt_line_17(self):
        if self.is_match(self.drop[1][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_17", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_17", self.drop[2][2])
                if self.is_match(self.drop[2][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_17", self.drop[2][2])

    def check_win_amt_line_18(self):
        if self.is_match(self.drop[1][0], self.drop[0][1]) and self.is_match(self.drop[0][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_18", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_18", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_18", self.drop[1][2])

    def check_win_amt_line_19(self):
        if self.is_match(self.drop[1][0], self.drop[2][1]) and self.is_match(self.drop[2][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_19", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_19", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_19", self.drop[1][2])

    def check_win_amt_line_20(self):
        if self.is_match(self.drop[0][0], self.drop[0][1]) and self.is_match(self.drop[0][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_20", self.drop[0][2])
            if self.is_match(self.drop[0][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_20", self.drop[0][2])
                if self.is_match(self.drop[0][2], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_20", self.drop[0][2])

    def check_win_amt_line_21(self):
        if self.is_match(self.drop[2][0], self.drop[2][1]) and self.is_match(self.drop[2][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_21", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_21", self.drop[2][2])
                if self.is_match(self.drop[2][2], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_21", self.drop[2][2])

    def check_win_amt_line_22(self):
        if self.is_match(self.drop[0][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_22", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_22", self.drop[2][2])
                if self.is_match(self.drop[2][2], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_22", self.drop[2][2])

    def check_win_amt_line_23(self):
        if self.is_match(self.drop[2][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_23", self.drop[0][2])
            if self.is_match(self.drop[0][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_23", self.drop[0][2])
                if self.is_match(self.drop[0][2], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_23", self.drop[0][2])

    def check_win_amt_line_24(self):
        if self.is_match(self.drop[1][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_24", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_24", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_24", self.drop[1][2])

    def check_win_amt_line_25(self):
        if self.is_match(self.drop[1][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_25", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_25", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_25", self.drop[1][2])

    def check_win_amt_line_26(self):
        if self.is_match(self.drop[0][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_26", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_26", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_26", self.drop[1][2])

    def check_win_amt_line_27(self):
        if self.is_match(self.drop[2][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_27", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_27", self.drop[1][2])
                if self.is_match(self.drop[1][2], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_27", self.drop[1][2])

    def check_win_amt_line_28(self):
        if self.is_match(self.drop[2][0], self.drop[2][1]) and self.is_match(self.drop[2][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_28", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_28", self.drop[1][2])
                if self.is_match(self.drop[0][3], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_28", self.drop[1][2])
    
    def check_win_amt_line_29(self):
        if self.is_match(self.drop[0][0], self.drop[0][1]) and self.is_match(self.drop[0][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_29", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_29", self.drop[1][2])
                if self.is_match(self.drop[2][3], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_29", self.drop[1][2])
    
    def check_win_amt_line_30(self):
        if self.is_match(self.drop[2][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_30", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_30", self.drop[2][2])
                if self.is_match(self.drop[2][3], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_30", self.drop[2][2])
    
    def check_win_amt_line_31(self):
        if self.is_match(self.drop[0][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_31", self.drop[0][2])
            if self.is_match(self.drop[0][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_31", self.drop[0][2])
                if self.is_match(self.drop[0][3], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_31", self.drop[0][2])
    
    def check_win_amt_line_32(self):
        if self.is_match(self.drop[0][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_32", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_32", self.drop[2][2])
                if self.is_match(self.drop[1][3], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_32", self.drop[2][2])
    
    def check_win_amt_line_33(self):
        if self.is_match(self.drop[2][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_33", self.drop[0][2])
            if self.is_match(self.drop[0][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_33", self.drop[0][2])
                if self.is_match(self.drop[1][3], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_33", self.drop[0][2])
    
    def check_win_amt_line_34(self):
        if self.is_match(self.drop[1][0], self.drop[0][1]) and self.is_match(self.drop[0][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_34", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_34", self.drop[1][2])
                if self.is_match(self.drop[0][3], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_34", self.drop[1][2])
    
    def check_win_amt_line_35(self):
        if self.is_match(self.drop[1][0], self.drop[2][1]) and self.is_match(self.drop[2][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_35", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_35", self.drop[1][2])
                if self.is_match(self.drop[2][3], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_35", self.drop[1][2])
    
    def check_win_amt_line_36(self):
        if self.is_match(self.drop[0][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_36", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_36", self.drop[1][2])
                if self.is_match(self.drop[1][3], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_36", self.drop[1][2])
    
    def check_win_amt_line_37(self):
        if self.is_match(self.drop[2][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_37", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_37", self.drop[1][2])
                if self.is_match(self.drop[1][3], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_37", self.drop[1][2])
    
    def check_win_amt_line_38(self):
        if self.is_match(self.drop[1][0], self.drop[0][1]) and self.is_match(self.drop[0][1], self.drop[0][2]):
            self.check_3_symbols("win_amount_line_38", self.drop[0][2])
            if self.is_match(self.drop[0][2], self.drop[0][3]):
                self.check_4_symbols("win_amount_line_38", self.drop[0][2])
                if self.is_match(self.drop[0][3], self.drop[0][4]):
                    self.check_5_symbols("win_amount_line_38", self.drop[0][2])
    
    def check_win_amt_line_39(self):
        if self.is_match(self.drop[1][0], self.drop[2][1]) and self.is_match(self.drop[2][1], self.drop[2][2]):
            self.check_3_symbols("win_amount_line_39", self.drop[2][2])
            if self.is_match(self.drop[2][2], self.drop[2][3]):
                self.check_4_symbols("win_amount_line_39", self.drop[2][2])
                if self.is_match(self.drop[2][3], self.drop[2][4]):
                    self.check_5_symbols("win_amount_line_39", self.drop[2][2])
    
    def check_win_amt_line_40(self):
        if self.is_match(self.drop[1][0], self.drop[1][1]) and self.is_match(self.drop[1][1], self.drop[1][2]):
            self.check_3_symbols("win_amount_line_40", self.drop[1][2])
            if self.is_match(self.drop[1][2], self.drop[1][3]):
                self.check_4_symbols("win_amount_line_40", self.drop[1][2])
                if self.is_match(self.drop[1][3], self.drop[1][4]):
                    self.check_5_symbols("win_amount_line_40", self.drop[1][2])

    def clear(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DELETE]:
            self.drop[0][0] = None
            self.drop[0][1] = None
            self.drop[0][2] = None
            self.drop[0][3] = None
            self.drop[0][4] = None
            self.drop[1][0] = None
            self.drop[1][1] = None
            self.drop[1][2] = None
            self.drop[1][3] = None
            self.drop[1][4] = None
            self.drop[2][0] = None
            self.drop[2][1] = None
            self.drop[2][2] = None
            self.drop[2][3] = None
            self.drop[2][4] = None

    def is_mouse_over_symbol(self, symbol_rect):
        mouse_pos = pygame.mouse.get_pos()
        return symbol_rect.collidepoint(mouse_pos)

    def remove_symbol_at_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        for row in range(len(self.drop)):
            for col in range(len(self.drop[row])):
                symbol = self.drop[row][col]
                if symbol is not None:
                    symbol_rect = pygame.Rect(col * 300, row * 300, 300, 300)
                    if self.is_mouse_over_symbol(symbol_rect):
                        self.drop[row][col] = None

                        
    def update(self, delta_time):
        self.separator()
        drop_surf = self.create_drop_surf()
        drag_surf = self.create_drag_surf()
        drop_pos_x = (1680 - drop_surf.get_width()) // 2
        drop_pos_y = ((1050 - drop_surf.get_height()) // 2) - 55
        drag_pos_x = (self.display_surface.get_size()[0] - 1325) / 2
        drag_pos_y = self.display_surface.get_size()[1] - 125
        self.display_surface.blit(drag_surf, (drag_pos_x, drag_pos_y))
        self.display_surface.blit(drop_surf, (drop_pos_x, drop_pos_y))
    
        symbol, x, y, board_type = self.get_square_under_mouse(self.drop, self.drag)
    
        if x is not None and y is not None:
            if board_type == 'drop':
                rect = (drop_pos_x + x * 300, drop_pos_y + y * 300, 300, 300)
            elif board_type == 'drag':
                rect = (drag_pos_x + x * 120, drag_pos_y + y * 120, 120, 120)  # Assuming 120 is the size for drag
            pygame.draw.rect(self.display_surface, (255, 0, 0, 50), rect, 2)
    
        mouse_click = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
    
        # Assuming mouse_click[0] is True when the button is pressed and False when released
        if mouse_click[0]:  # Left mouse button is pressed
            if self.selected_symbol is None:  # Select symbol if none is selected
                if symbol is not None:
                    self.selected_symbol = (symbol, x, y, board_type)
            # Removed the code to move the symbol here
        else:  # This block now executes when the left mouse button is released
            if self.selected_symbol is not None:  # Check if a symbol is selected
                selected_symbol, sx, sy, sboard_type = self.selected_symbol
                if board_type == 'drop' and sboard_type == 'drag':  # Move the symbol if the conditions are met
                    img100_to_img = {"A_100":"A_300",
                                     "Ankh_100":"Ankh_300",
                                     "J_100":"J_300",
                                     "K_100":"K_300",
                                     "Mask_100":"Mask_300",
                                     "Q_100":"Q_300",
                                     "Scarab_100":"Scarab_300",
                                     "Sfnx_100":"Sfnx_300",
                                     "Wild_100":"Wild_300",
                                     "Stone_100":"Stone_300",
                                     "Gem_100":"Gem_300"}
                    self.drop[y][x] = img100_to_img[self.drag[sy][sx]]
                    self.selected_symbol = None
            else:
                self.selected_symbol = None  # Deselect the symbol if the mouse is released without moving

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right-click
                self.remove_symbol_at_mouse()
    
        self.draw_drop_pieces(self.display_surface, self.drop, drop_surf)
        self.frame()
        self.draw_drag_pieces(self.display_surface, self.drag)
        self.draw_selector(self.display_surface, symbol, x, y)
        self.spin_count()
        self.win_amount_display()
        self.save_input()
        self.template()
        self.clear()
        self.for_preview()
        self.read_existing_spin_counts(self.input_file)