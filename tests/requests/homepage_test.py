from redrover import *


class HomepageTest(RedRoverLiveTest):

  subject = page

  @before
  def setUp(self):
    visit('home')

  @describe
  def the_homepage(self):
    it.should(have_selector, '#redrover')
    its('title').should(be, "RedRover")
