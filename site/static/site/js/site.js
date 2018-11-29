var terms = $("ul.home-jumbo-ul0 li");
var init=false;// to force the initial text when slide changes
var actualSlide=0;

function rotateTerm() {
  if (init)
  {
	  var ct =  0;
  }
  else
  {
	  var ct = $("#rotate".concat(actualSlide.toString())).data("term") || 0;
  }
  
  init=false;
  if (ct < terms.length -1)
  {
	  $("#rotate".concat(actualSlide.toString())).data("term",ct == terms.length -1 ? 0 : ct + 1).text(terms.eq([ct]).text()).fadeIn().delay(4000).fadeOut(200, rotateTerm);
  }else
  {
	  $("#rotate".concat(actualSlide.toString())).data("term",ct == terms.length -1 ? 0 : ct + 1).text(terms.eq([ct]).text()).fadeIn().delay(4000).fadeOut(200,rotateTerm);
  }
}


$("#myCarousel").on('slide.bs.carousel', function (event) {

	  var active = $(event.target).find('.carousel-inner > .item.active');
	  var from = active.index();
	  var next = $(event.relatedTarget);
	  var to = next.index();
	  actualSlide=to;
	  var direction = event.direction;
	  init=true;// to force the initial text when slide changes
	  if (to==0)
	  {
		  terms = $("ul.home-jumbo-ul0 li");
		  
		  
	  }else if(to==1)
	  {
		  terms = $("ul.home-jumbo-ul1 li");
	  }
	  $(rotateTerm);
});



$(rotateTerm);