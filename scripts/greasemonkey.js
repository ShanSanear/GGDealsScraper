// ==UserScript==
// @name     GGDealsScrapper
// @version  1
// @grant    none
// @require https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js
// @include https://barter.vg/*
// ==/UserScript==


var input=document.createElement("input");
input.type="button";
input.value="Get games prices";
input.onclick = showAlert;
input.setAttribute("style", "font-size:18px");
var offerForm = $("#offer");
if (!offerForm.length) {
  offerForm = $("#exchanges");
}
console.log(offerForm);
offerForm.before(input);
$.ajaxSetup({
    async: true
});


async function getGameLowestPrice(game) {
  let mainUrl = "http://127.0.0.1:8000/game/";
  let gameFullUrl = mainUrl + game;
  let prices = [];
  let ret;
  await $.getJSON(gameFullUrl, function(data) {
    for (var i = 0; i < data['prices'].length; i++) {
      prices.push(parseFloat(data['prices'][i]['price'].replace(",", ".")));
    }
    console.log("Got it for " + game);
    ret = prices.length > 0 ? Math.min(... prices) : "https://gg.deals/games/?title=" + game;
  });
  return ret + "";
}

async function showAlert()
{
  var all_trads = $(".tradables .tradables_info")
  console.log("Getting tradables: " + all_trads.length);
  var gamePrice;
  for (var i=0; i < all_trads.length; i++){
    var trad = all_trads[i];

    console.log(trad);
    try{
    	var gameName = $(trad).children("strong").children("a")[0].innerText
      }
    catch(error) {
      console.log("Error: " + error);
      var gameName = $(trad).children("a")[0].innerText
    }
    console.log("Game name: " +gameName)
    var externalLinkNode = $(trad).children("a")[0];
    try{
    	gamePrice = await getGameLowestPrice(gameName);
    }
   	catch {
      console.log("Error when trying to get game price for " + gameName);
      gamePrice = "https://gg.deals/games/?title=" + gameName + "/"
  }
    if (!gamePrice.includes("http")) {
      console.log("Http link");
      var textWithPrice = document.createElement("span");
      var text = document.createTextNode(gamePrice + "zł");
      textWithPrice.appendChild(text);
      externalLinkNode.after(textWithPrice);
    } else {
      console.log("Non http link for " + gameName + " with price: " + gamePrice);
      var linkObject = document.createElement("a");
      var textNode = document.createTextNode("  GG Deals link: " + gameName);
      linkObject.appendChild(textNode);
      linkObject.href = gamePrice;
      externalLinkNode.after(linkObject);
    }
    console.log("Game: " + gameName + " has a lowest price of: " + gamePrice);

  }

}