// FICTION GENERATOR BY ROSS GOODWIN
// http://rossgoodwin.com/ficgen


// paths and such
String sysPath = "/Users/rg/Projects/plotgen/new/plotgen/";
String novPath = "/Users/rg/Google Drive/novels/";
String novelTitle = "Two Paths";
String firstName = "Name";
String lastName = "Surname";
String toEmail = "ross.goodwin@gmail.com";
boolean finished = false;

// time to go!
int beepBeep;

// fonts
PFont gotham32;
PFont gotham18;


// GUI Elements
PVector title;

PVector generateButton;
PShape generateSymbol;

// PVector upperLeft;

void setup() {
  size(displayWidth, displayHeight);
  gotham32 = loadFont("Gotham-Book-32.vlw");
  gotham18 = loadFont("Gotham-Book-18.vlw");
  
  title = new PVector(width/2, 20);
  // upperLeft = new PVector(0, 68);
  
  generateButton = new PVector(width/2, height-100);
  generateSymbol = loadShape("generate_symbol.svg");
  
}

void draw() {
  background(236, 240, 241);
  
  // headline and border
  textFont(gotham32);
  textAlign(CENTER, TOP);
  fill(108, 122, 137);
  //fill(242,38,19);
  noStroke();
  text("FICTION GENERATOR", title.x, title.y);
  
  // fill(108, 122, 137);
  // noStroke();
  // rectMode(CORNER);
  // rect(upperLeft.x, upperLeft.y, width, 2);
  
  // generate button
  noStroke();
  fill(231, 76, 60);
  rectMode(CENTER);
  rect(generateButton.x, generateButton.y, 100, 100);
  
  shapeMode(CENTER);
  fill(255);
  noStroke();
  shape(generateSymbol, generateButton.x, generateButton.y-3, 65, 65);
  
  if (finished) {
    fill(0, 20);
    rectMode(CENTER);
    rect(generateButton.x, generateButton.y, 100, 100);
  } else {
    fill(0, 20);
    rectMode(CENTER);
    rect(generateButton.x, generateButton.y+45, 100, 10);
  }
  
  
  
  // textFont(gotham18);
  // textAlign(CENTER, CENTER);
  // fill(255);
  // noStroke();
  // text("", generateButton.x, generateButton.y-3);
  
  
  
  if (finished && frameCount >= beepBeep) {
    // filenames
    String pdfName = novelTitle + ".pdf";
    String auxName = novelTitle + ".aux";
    String logName = novelTitle + ".log";
    String outName = novelTitle + ".out";
    
    // take out the trash (remove log files)
    String[] paramsRm = {"rm", auxName, logName, outName};
    exec(paramsRm);
    
    // move the cargo (novelTitle.pdf goes to Google Drive/novels/)
    String[] paramsMv = {"mv", pdfName, novPath};
    exec(paramsMv);
    
    // open the PDF
    open(novPath+pdfName);
    
    // send email
    String[] paramsNovel = {"python", sysPath+"sendnovel.py", toEmail, novPath+pdfName};
    exec(paramsNovel);
    
    // speak
    String talk = "Thanks for the inspiration, " + firstName + ". I just wrote your story, and I think it's a real page turner. No spoilers though. You'll have to read it for yourself. I sent you the PDF. Enjoy!";
    String[] paramsSay = {"say", talk};
    exec(paramsSay);
    
    // set finished boolean to false (so that it doesn't keep running this part)
    finished = false;
  }
}

void mousePressed() {
  
  if (mouseX > generateButton.x-50 && mouseX < generateButton.x+50 && mouseY > generateButton.y-50 && mouseY < generateButton.y+50) {
  
    beepBeep = frameCount + int(frameRate*6);
  
    String novelFile = sysPath + "output/" + novelTitle + ".tex";
    
    String[] paramsNovel = {"python", sysPath+"novelizer_icm.py", novelTitle, firstName+" "+lastName};
    exec(paramsNovel);
    
    String[] paramsPDF = {"/usr/texbin/pdflatex", novelFile};
    exec(paramsPDF);
    
    finished = true;
  }
  
}
