var Language = function(code, name) {
  this.code = code;
  this.name = name;
};
var languages = [
  new Language("sq", "Albanian"),
  new Language("ar", "Arabian"),
  new Language("hy", "Armenian"),
  new Language("az", "Azeri"),
  new Language("be", "Belarusian"),
  new Language("bs", "Bosnian"),
  new Language("bg", "Bulgarian"),
  new Language("ca", "Catalan"),
  new Language("hr", "Croatian"),
  new Language("cs", "Czech"),
  new Language("zh", "Chinese"),
  new Language("da", "Danish"),
  new Language("nl", "Dutch"),
  new Language("en", "English"),
  new Language("et", "Estonian"),
  new Language("fi", "Finnish"),
  new Language("fr", "French"),
  new Language("ka", "Georgian"),
  new Language("de", "German"),
  new Language("el", "Greek"),
  new Language("he", "Hebrew"),
  new Language("hu", "Hungarian"),
  new Language("is", "Icelandic"),
  new Language("id", "Indonesian"),
  new Language("it", "Italian"),
  new Language("ja", "Japanese"),
  new Language("ko", "Korean"),
  new Language("lv", "Latvian"),
  new Language("lt", "Lithuanian"),
  new Language("mk", "Macedonian"),
  new Language("ms", "Malay"),
  new Language("mt", "Maltese"),
  new Language("no", "Norwegian"),
  new Language("pl", "Polish"),
  new Language("pt", "Portuguese"),
  new Language("ro", "Romanian"),
  new Language("ru", "Russian"),
  new Language("es", "Spanish"),
  new Language("sr", "Serbian"),
  new Language("sk", "Slovak"),
  new Language("sl", "Slovenian"),
  new Language("sv", "Swedish"),
  new Language("th", "Thai"),
  new Language("tr", "Turkish"),
  new Language("uk", "Ukrainian"),
  new Language("vi", "Vietnamese")
];
var apiKey = "trnsl.1.1.20150817T004045Z.071173432f8f6a05.c3a0c33a0d0e1daf201905afafa6eb251c8f2e62";

var run = function() {
  var langNum = languages.length;
  var lastLang = "en";
  var currString = $scope.data.input;
  for (var i = 0; i < $scope.data.chainLength; i++) {
    var randNum = 0;
    var newLang = {};
    // do {
    randNum = Math.floor((Math.random() * langNum));
    newLang = languages[randNum].code;
    // }
    // while(newLang === lastLang);
    currString = translate(currString, lastLang, newLang);
    lastLang = newLang;
    $scope.data.steps.push(currString);
  }
  currString = translate(currString, lastLang, "en");
  //console.log(currString);
  $scope.data.result = currString;
};

var translate = function(inText, fromLang, toLang) {
  var outString = "";
  var result = {};
  var request = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=";
  request += apiKey + "&lang=" + fromLang + "-" + toLang + "&text=" + encodeURIComponent(inText);
  console.log(request);
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", request, false);
  xmlHttp.send(null);
  result = JSON.parse(xmlHttp.responseText);

  if (result["code"] === 200) {
    outString = result["text"];
  } else {
    outString = inString;
  }
  return outString;
};
