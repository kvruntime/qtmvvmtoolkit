from .UI.UIPageNav import Ui_PageNav
from PyQt6.QtWidgets import QWidget
from qtmvvmkit.navigations.StackWidgetRouter import StackWidgetRouter
from qtmvvmkit.widgets.navbutton import NavButton


class PageNav(Ui_PageNav, QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        
        self.router = StackWidgetRouter(self.routeView)
        self.router.registerRoute("page1", self.page1)
        self.router.registerRoute("page2", self.page2)
        self.router.registerRoute("page3", self.page3)
        self.router.registerRoute("/page4", self.page4)

        self.buttonPage1 = NavButton(text="Page1",router= self.router,path= "page1")
        self.buttonPage2 = NavButton(text="Page2",router= self.router,path= "page2")
        self.buttonPage3 = NavButton(text="Page3",router= self.router,path= "page3")
        self.buttonPage4.add_router(self.router)
        self.buttonPage4.setText("-Page4-")
        self.buttonPage4.set_path("/page4")
        self.layoutNavBar.addWidget(self.buttonPage1)
        self.layoutNavBar.addWidget(self.buttonPage2)
        self.layoutNavBar.addWidget(self.buttonPage3)
        self.layoutNavBar.addWidget(self.buttonPage4)
    pass
