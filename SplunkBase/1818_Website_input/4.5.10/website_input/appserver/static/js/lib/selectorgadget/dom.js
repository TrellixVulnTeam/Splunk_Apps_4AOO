function DomPredictionHelper(){}DomPredictionHelper.prototype=new Object();DomPredictionHelper.prototype.recursiveNodes=function(a){var b;if(a.nodeName&&a.parentNode&&a!=document.body){b=this.recursiveNodes(a.parentNode)}else{b=new Array()}b.push(a);return b};DomPredictionHelper.prototype.escapeCssNames=function(a){if(a){try{return a.replace(/\s*sg_\w+\s*/g,"").replace(/\\/g,"\\\\").replace(/\./g,"\\.").replace(/#/g,"\\#").replace(/\>/g,"\\>").replace(/\,/g,"\\,").replace(/\:/g,"\\:")}catch(b){console.log("---");console.log("exception in escapeCssNames");console.log(a);console.log("---");return""}}else{return""}};DomPredictionHelper.prototype.childElemNumber=function(b){var a=0;while(b.previousSibling&&(b=b.previousSibling)){if(b.nodeType==1){a++}}return a};DomPredictionHelper.prototype.pathOf=function(d){var b=this.recursiveNodes(d);var a=this;var h="";for(var c=0;c<b.length;c++){var g=b[c];if(g){h+=g.nodeName.toLowerCase();var f=g.id&&a.escapeCssNames(new String(g.id));if(f&&f.length>0){h+="#"+f}if(g.className){jQuery.each(g.className.split(/ /),function(){var e=a.escapeCssNames(this);if(this&&e.length>0){h+="."+e}})}h+=":nth-child("+(a.childElemNumber(g)+1)+")";h+=" "}}if(h.charAt(h.length-1)==" "){h=h.substring(0,h.length-1)}return h};DomPredictionHelper.prototype.commonCss=function(g){try{var a=new diff_match_patch()}catch(d){throw"Please include the diff_match_patch library."}if(typeof g=="undefined"||g.length==0){return""}var f={};var b=this.encodeCssForDiff(g,f);var c=b.pop();jQuery.each(b,function(i){var h=a.diff_main(c,this);c="";jQuery.each(h,function(){if(this[0]==0){c+=this[1]}})});return this.decodeCss(c,f)};DomPredictionHelper.prototype.tokenizeCss=function(a){var e=false;var g="";var f=[];var a=a.replace(/,/," , ").replace(/\s+/g," ");var d=a.length;var h="";for(var b=0;b<d;b++){h=a[b];if(e){e=false}else{if(h=="\\"){e=true}else{if(h=="."||h==" "||h=="#"||h==">"||h==":"||h==","){if(g.length>0){f.push(g)}g=""}}}g+=h;if(h==" "||h==","){f.push(g);g=""}}if(g.length>0){f.push(g)}return f};DomPredictionHelper.prototype.decodeCss=function(c,d){var a=this.invertObject(d);var b="";jQuery.each(c.split(""),function(){b+=a[this]});return this.cleanCss(b)};DomPredictionHelper.prototype.encodeCssForDiff=function(a,d){var c=50;var b=this;var e=[];jQuery.each(a,function(){var f=new String();jQuery.each(b.tokenizeCss(this),function(){if(!d[this]){d[this]=String.fromCharCode(c++)}f+=d[this]});e.push(f)});return e};DomPredictionHelper.prototype.simplifyCss=function(i,a,g){var k=this;var d=k.tokenizeCss(i);var h="";if(k.selectorGets("all",a,i)&&k.selectorGets("none",g,i)){h=i}for(var j=0;j<4;j++){for(var b=0;b<d.length;b++){var f=d[b].substring(0,1);if(k.wouldLeaveFreeFloatingNthChild(d,b)){continue}if((j==0&&f==":")||(j==1&&f!=":"&&f!="."&&f!="#"&&f!=" ")||(j==2&&f==".")||(j==3&&f=="#")){var e=d[b];d[b]="";var c=k.cleanCss(d.join(""));if(c==""){d[b]=e;continue}if(k.selectorGets("all",a,c)&&k.selectorGets("none",g,c)){h=c}else{d[b]=e}}}}return k.cleanCss(h)};DomPredictionHelper.prototype.wouldLeaveFreeFloatingNthChild=function(b,a){return(((a-1>=0&&b[a-1].substring(0,1)==":")&&(a-2<0||b[a-2]==" ")&&(a+1>=b.length||b[a+1]==" "))||((a+1<b.length&&b[a+1].substring(0,1)==":")&&(a+2>=b.length||b[a+2]==" ")&&(a-1<0||b[a-1]==" ")))};DomPredictionHelper.prototype.cleanCss=function(a){return a.replace(/\>/," > ").replace(/,/," , ").replace(/\s+/g," ").replace(/^\s+|\s+$/g,"").replace(/,$/,"")};DomPredictionHelper.prototype.getPathsFor=function(a){var b=this;var c=[];jQuery.each(a,function(){if(this&&this.nodeName){c.push(b.pathOf(this))}});return c};DomPredictionHelper.prototype.predictCss=function(c,e){var a=this;if(c.length==0){return""}var f=a.getPathsFor(c);var h=a.getPathsFor(e);var b=a.commonCss(f);var d=a.simplifyCss(b,f,h);if(d.length>0){return d}var g="";jQuery.each(c,function(){g=a.pathOf(this)+", "+g});g=a.cleanCss(g);return a.simplifyCss(g,f,h)};DomPredictionHelper.prototype.fragmentSelector=function(a){var b=this;var c=[];jQuery.each(a.split(/\,/),function(){var d=[];jQuery.each(b.cleanCss(this).split(/\s+/),function(){d.push(b.tokenizeCss(this))});c.push(d)});return c};DomPredictionHelper.prototype.selectorBlockMatchesSelectorBlock=function(c,b){for(var a=0;a<c.length;a++){if(jQuery.inArray(c[a],b)==-1){return false}}return true};DomPredictionHelper.prototype.selectorGets=function(e,g,f){var c=this;var b=true;if(g.length==0&&e=="all"){return false}if(g.length==0&&e=="none"){return true}var d=c.fragmentSelector(f);var a=[];jQuery.each(g,function(){a.push(c.fragmentSelector(this)[0])});jQuery.each(d,function(){if(!b){return}var h=this;jQuery.each(a,function(i){if(!b||this==""){return}if(c._selectorGets(this,h)){if(e=="none"){b=false}a[i]=""}})});if(e=="all"&&a.join("").length>0){b=false}return b};DomPredictionHelper.prototype._selectorGets=function(d,f){var c=false;var a=d.length-1;for(var b=f.length-1;b>-1;b--){if(c){break}if(b==f.length-1){if(!this.selectorBlockMatchesSelectorBlock(f[b],d[a])){c=true}a--}else{var e=false;while(a>-1&&!e){e=this.selectorBlockMatchesSelectorBlock(f[b],d[a]);a--}if(!e){c=true}}}return !c};DomPredictionHelper.prototype.invertObject=function(a){var b={};jQuery.each(a,function(c,d){b[d]=c});return b};DomPredictionHelper.prototype.cssToXPath=function(a){var e=this.tokenizeCss(a);if(e[0]&&e[0]==" "){e.splice(0,1)}if(e[e.length-1]&&e[e.length-1]==" "){e.splice(e.length-1,1)}var d=[];var b="";for(var c=0;c<e.length;c++){if(e[c]==" "){b+=this.cssToXPathBlockHelper(d);d=[]}else{d.push(e[c])}}return b+this.cssToXPathBlockHelper(d)};DomPredictionHelper.prototype.cssToXPathBlockHelper=function(g){if(g.length==0){return"//"}var a="//";var h=g[0].substring(0,1);if(h==","){return" | "}if(jQuery.inArray(h,[":","#","."])!=-1){a+="*"}var e=[];var d=null;for(var b=0;b<g.length;b++){var f=g[b];h=f.substring(0,1);var c=f.substring(1);if(h==":"){if(d=c.match(/^nth-child\((\d+)\)$/)){e.push("(((count(preceding-sibling::*) + 1) = "+d[1]+") and parent::*)")}}else{if(h=="."){e.push('contains(concat( " ", @class, " " ), concat( " ", "'+c+'", " " ))')}else{if(h=="#"){e.push('(@id = "'+c+'")')}else{if(h==","){}else{a+=f}}}}}if(e.length>0){a+="["}for(var b=0;b<e.length;b++){a+=e[b];if(b<e.length-1){a+=" and "}}if(e.length>0){a+="]"}return a};