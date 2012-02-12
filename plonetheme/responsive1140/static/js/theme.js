function initializeplonethemeresponsive1140(){
  /* put last class on global nav */
  tabs = $('#portal-globalnav li') ;
  if (tabs.length>0) {
    $(tabs[tabs.length-1]).addClass('last');
  }
}
jQuery(initializeplonethemeresponsive1140);
