from math import sin, cos, pi

import pygame

displayWidth = 640
displayHeight = 480
fpsLimit = 100


def sinInterpolation(start, end, steps=100):
    values = [start]
    delta = end - start
    for i in range(1, steps):
        n = (pi / 2.0) * (i / float(steps - 1))
        values.append(start + delta * sin(n))
    return values


class RotatingMenu:
    def __init__(self, x, y, radius, arc=pi * 2, defaultAngle=0, wrap=True):
        """
        @param x:
            The horizontal center of this menu in pixels.
        
        @param y:
            The vertical center of this menu in pixels.
        
        @param radius:
            The radius of this menu in pixels(note that this is the size of
            the circular path in which the elements are placed, the actual
            size of the menu may vary depending on item sizes.
        @param arc:
            The arc in radians which the menu covers. pi*2 is a full circle.
        
        @param defaultAngle:
            The angle at which the selected item is found.
        
        @param wrap:
            Whether the menu should select the first item after the last one
            or stop.
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.arc = arc
        self.defaultAngle = defaultAngle
        self.wrap = wrap

        self.rotation = 0
        self.rotationTarget = 0
        self.rotationSteps = []  # Used for interpolation

        self.items = []
        self.selectedItem = None
        self.selectedItemNumber = 0

    def addItem(self, item):
        self.items.append(item)
        if len(self.items) == 1:
            self.selectedItem = item

    def selectItem(self, itemNumber):
        if self.wrap == True:
            if itemNumber > len(self.items) - 1: itemNumber = 0
            if itemNumber < 0: itemNumber = len(self.items) - 1
        else:
            itemNumber = min(itemNumber, len(self.items) - 1)
            itemNumber = max(itemNumber, 0)

        self.selectedItem.deselect()
        self.selectedItem = self.items[itemNumber]
        self.selectedItem.select()

        self.selectedItemNumber = itemNumber

        self.rotationTarget = - self.arc * (itemNumber / float(len(self.items) - 1))


        # if self.selectedItemNumber == 0:

        if self.rotationTarget >= pi:
            self.rotationTarget = pi + self.rotationTarget
        self.rotationSteps = sinInterpolation(self.rotation, self.rotationTarget, 45)
        print(self.selectedItemNumber)
        print(self.rotation, self.rotationTarget)
        print(self.rotationSteps)

    def rotate(self, angle):
        """@param angle: The angle in radians by which the menu is rotated.
        """
        for i in range(len(self.items)):
            item = self.items[i]
            n = i / float(len(self.items) - 1)
            rot = self.defaultAngle + angle + self.arc * n

            item.x = self.x + cos(rot) * self.radius
            item.y = self.y + sin(rot) * self.radius

            if self.selectedItemNumber == 2:
                self.items[0].x = self.x - cos(rot * 2) * self.radius
                self.items[0].y = self.y - sin(rot * 2) * self.radius
            if self.selectedItemNumber == 0:
                self.items[2].x = self.x + cos(rot * 2) * self.radius
                self.items[2].y = self.y + sin(rot * 2) * self.radius

    def update(self):
        if len(self.rotationSteps) > 0:
            self.rotation = self.rotationSteps.pop(0)
            self.rotate(self.rotation)

    def draw(self, display):
        """@param display: A pyGame display object
        """
        for item in self.items:
            item.draw(display)


class MenuItem:
    def __init__(self, text):
        self.text = text

        self.defaultColor = (255, 255, 255)
        self.selectedColor = (255, 0, 0)
        self.color = self.defaultColor

        self.x = 0
        self.y = 0  # The menu will edit these

        self.font = pygame.font.Font(None, 50)
        self.image = self.font.render(self.text, True, self.color)
        size = self.font.size(self.text)
        self.xOffset = size[0] / 2
        self.yOffset = size[1] / 2

    def select(self):
        """Just visual stuff"""
        self.color = self.selectedColor
        self.redrawText()

    def deselect(self):
        """Just visual stuff"""
        self.color = self.defaultColor
        self.redrawText()

    def redrawText(self):
        self.font = pygame.font.Font(None, 50)
        self.image = self.font.render(self.text, True, self.color)
        size = self.font.size(self.text)
        self.xOffset = size[0] / 2
        self.yOffset = size[1] / 2

    def draw(self, display):
        display.blit(self.image, (self.x - self.xOffset, self.y - self.yOffset))


def main():
    pygame.init()

    display = pygame.display.set_mode((displayWidth, displayHeight))
    clock = pygame.time.Clock()

    menu = RotatingMenu(x=320, y=displayHeight - 50, radius=200, arc=pi, defaultAngle=3 * pi / 2.0)

    menu.addItem(MenuItem("Encoding"))
    menu.addItem(MenuItem("Decoding"))
    menu.addItem(MenuItem("Learning"))
    menu.selectItem(1)

    # Loop
    while True:
        # Handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    menu.selectItem(menu.selectedItemNumber - 1)
                if event.key == pygame.K_RIGHT:
                    menu.selectItem(menu.selectedItemNumber + 1)

        # Update stuff
        menu.update()

        # Draw stuff
        display.fill((0, 0, 0))
        menu.draw(display)
        pygame.display.flip()  # Show the updated scene
        clock.tick(fpsLimit)  # Wait a little


if __name__ == "__main__":
    main()
