import arcade

arcade.open_window(600, 600, "Drawing Samples")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_lrbt_rectangle_filled(0, 600, 0, 300, arcade.csscolor.GREEN)

arcade.draw_lrbt_rectangle_filled(90, 110, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100,350,30,arcade.csscolor.DARK_GREEN)
arcade.draw_lbwh_rectangle_filled(190, 290, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)
arcade.draw_lbwh_rectangle_filled(290, 290, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)
arcade.draw_lbwh_rectangle_filled(390, 290, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)
arcade.draw_lbwh_rectangle_filled(490, 290, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400), (480, 360), (470, 320), (530, 320), (520, 360)),arcade.csscolor.DARK_GREEN)

arcade.draw_circle_filled(500, 550, 30, arcade.csscolor.YELLOW)
arcade.draw_line(400,550,600,550, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500,450,500,650, arcade.csscolor.YELLOW, 3)
arcade.draw_line(450, 500, 550, 600, arcade.csscolor.YELLOW, 3)
arcade.draw_line(450, 600, 550, 500, arcade.csscolor.YELLOW, 3)

arcade.draw_text("Arbor Day - Plant a Tree!", 150, 230, arcade.csscolor.BLACK, 24)




arcade.finish_render()

arcade.run()