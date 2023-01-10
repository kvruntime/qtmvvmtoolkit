from .UI.UIPageNav import Ui_PageNav
from PyQt6.QtWidgets import QWidget
from mvvmkit.navigations.StackWidgetRouter import StackWidgetRouter
from mvvmkit.navigations.ButtonNav import NavButton


class PageNav(Ui_PageNav, QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        
        self.router = StackWidgetRouter(self.routeView)
        self.router.register_route("page1", self.page1)
        self.router.register_route("page2", self.page2)
        self.router.register_route("page3", self.page3)
        self.router.register_route("/page4", self.page4)

        self.buttonPage1 = NavButton(text="Page1",router= self.router,path= "page1")
        self.buttonPage2 = NavButton(text="Page2",router= self.router,path= "page2")
        self.buttonPage3 = NavButton(text="Page3",router= self.router,path= "page3")
        self.buttonPage4.addRouter(self.router)
        self.buttonPage4.setText("-Page4-")
        self.buttonPage4.setPath("/page4")
        self.layoutNavBar.addWidget(self.buttonPage1)
        self.layoutNavBar.addWidget(self.buttonPage2)
        self.layoutNavBar.addWidget(self.buttonPage3)
        self.layoutNavBar.addWidget(self.buttonPage4)
    pass
