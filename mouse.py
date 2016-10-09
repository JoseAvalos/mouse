#!/usr/bin/env python 
import pygame
import rospy

from geometry_msgs.msg import Vector3
class MainWindow(object):

    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Game')
        pygame.mouse.set_visible(True)
        vec = Vector3(1, 2, 3)
        try:
            pub = rospy.Publisher('mouse', Vector3, queue_size=1)
            rospy.init_node('node_mouse', anonymous=True)
            rate = rospy.Rate(10) # 10hz
            screen = pygame.display.set_mode((640,480), 0, 32)
            pygame.mixer.init()
            a=0 ,0 ,0
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                        #print pygame.mouse.get_pos()
                        a = pygame.mouse.get_pressed()
                print a
                vec.x=a[0]
                vec.y=a[1]
                vec.z=a[2]
                pub.publish(vec)
            pygame.mixer.quit()
            pygame.quit()

        except rospy.ROSInterruptException:
            pass

MainWindow()