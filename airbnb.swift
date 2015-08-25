class dragAndDropController: UIViewController {
  @IBOutlet var object: UIImageView
  @IBOutlet var trash: UIImageView
  var startingLocation: CGPoint = CGPoint.ZeroPoint

  override viewDidLoad() {
     let panGesture: UIPanGestureRecognizer(target: self, action:Selector:"dragObject:")
     object.addGestureRecognizer(panGesture)
  }

  func dragObject(recognizer: UIPanGestureRecognizer) {
     switch(recognizer.state) {
       case .Began:
         startingLocation = object.center
       case .Changed:
         let translation = recognizer.translationInView(self.view) // returns the translation from the starting location
         recognizer.view!.center = CGPointMake(startingLocation.x + translation.x, startingLocation.y + translation.y)
       case .Ended:
         if (object.frame.CGRectIntersectsRect(trash.frame)) {
            object.removeFromSuperview()
         } else {
            object.center = startingLocation
         }
     }
  }
}

iOS Team @Airbnb ~ 13 people

3 subteams
  1. Experience Architecture - infrastructure
  2. Design language + reusable components (both iOS and Android)
  3. Mobile Conversion (improving conversion on mobile - searching, sharing)

Francis's story
  Homebrew stuff for the iPod Touch
  Jailbreak software (bluetooth, saving YT videos) - hacky projects that improved functionality of system iPod apps
  Why AirBnb?
    The culture (core values + strong reliance on onsite interviews to really get to know applicants)
    Welcoming receptive folk
