function showSub(){
	var gu = document.getElementById("GuID");
	var dong = document.getElementById("DongID");
	var searchText;
	var val;
	var valDong;
	var changeItme;
	var gangnam =["Gap","Nonhyun","Daechi","Dogok","Samdong","Seogok","Suseo","Sinsa","Apgujeong","Yeoksam","Yulhyun","Ilwon ","Jagokdong","Cheongdam"];
	var gangdong = ["Gangil","Godeok","Gil ","Dunchon","Myung","Sangil","Sungnae","Amasa","Cheonho"];
	var gangbuk = ["Miada","Throb","Feeder","Wuyo"];
	var gangseo = ["Gayang","Gwahdae","Airport","Haehee","Mine","Dichon","Magok","Yongchan","Ogok","Biceps","Outsourcing","Hagok"];
	var gwanwak = ["Nam Hyun","Bongcheon","Sunrim "];
	var gwangjin = ["Gwangjang","Kudu","Gunja","Neong","Jayang","Jungok","Gyeong"];
	var guro = ["Garibong","Gongbong","Gojuck","Guro","Gung","Shindorim","Ohryu","Onsu","Chengwang","hyang"];
	var geumcheon = ["Gasan","Doksan","Sajin"];
	var nowon = ["Gongneung","Sanggye ","Wolgye","Junggae","Haegye"];
	var dobong = ["Dobong","Bang","Sukmun ","Chang"];
	var dongdaemoon = ["Dapsipli","Sinsul","Yongdu","LeeMoon","Jangan","Jeonbong ","Jeagi","Chengrangli","Fagi","Fhigeung"];
	var dongjak = ["Noryangjin","Sadang","Sang","ShinDaebang","Heukseok","Daebang"];
	var Mapo = ["Gongdeok","Gusu","Nogosan","Dangin","Dangin","Daeheung","Dohwa","Donggyo","Mapo ","Sangsu","Sangam","Seogyo","Seongsan","Shin ","Sinsu","Sinjeong","Ahhyun","Yeonnam","Sori","Yonggang","Taejung","Hae","Hodge","Hapjung","Jung",];
	var seodaemon = ["Bockgajwa","Nangchung","Namgajwa","Bockyaheun","Shinchon","Yeon","Youngchun","Okcheon","Hong Eun","Hongjeong","Chunyeon"];
	var seocho = ["Naegock","Bangbae","Seocho","Yangjae","Yeonggok","Jamson","Banpo"];
	var seongdong = ["Majang","Sangyeong","Songjeong","Oshu","Yongdo","Jongbong","Hwang "];
	var seongbuk = ["Gilgyoung","Donam","Seokgu","Seongbuk","Zhang Guo","Jungnung","Jongam",];
	var songpa = ["Pungnam","Garak","Gyeon","Machong","Munjeong","Bang","Samjeong","Seochun","Songpa","Shinchon","Ohgum","Jamsil","Jang Ji"];
	var yangcheon = ["Sinwol","Sinjeong","Mock"];
	var yeongdeunpo = ["Dangsan","Daelim","Dorim","Shin Gil","Yangpyoung","Yeongdeungpo"];
	var yongsan = ["Galwol","Namyong","Bokwang","Yongmun ","Seobinggo","Leechon","Itaewon","Hannam","Hyochang","Hoam"];
	var eunpyeong = ["Galhyun","Gusan","Nockbun","Daejong","BulGwang ","Suseak","Sinsa","Yuckcheon","Yeumyang","Jungsan","Jingwang"];
	var jongro = ["Gaho","Gungi","Gongpyeong","Geonam","Gugi","Nackone","Donei","Meo","Moyack","Bongik","Buam","Sajik","Samcheong","sogeck","Sungin","Shinhyo","Yeahgi","Okin","Wally","Waoryong","Wonnam","Wonsa","Lee Hwa","Insa","In","Jang Sa","Juckseon","Changsin","Cheongun","Cheongjin","Chungsin","Tongin","Pyungchang","Hyehwa","Hyoja","Hyoje"];
	var jung = ["Sogong","Shindang","Jeong","Jungrim","Hwang Hak"];
	var jungang = ["Mangoo","Munmock","Mock","Sangbong","Shin ","Junghwa"];
	
	// Debugging 중일때는 주석해놓을 것. 
// for(i=0; i<gu.options.length; i++) {
//     if(gu.options[i].selected === true) {
//         val = gu.options[i].value;         // 어떤 값이 선택되었는지 확인해보고 
// 		break;								// 선택된 값을 val 에 저장.
//     }
// }
	val =1 // 1로 디버깅 디폴드 모드
	if(val == 1 )
		{
			changeItme = gangnam;   //1이 선택되었을 경우에 
		}
	else if(val == 2){changeItme = gangdong;}
	else if(val == 3){changeItme = gangbuk;}
	else if(val == 4){changeItme = gangseo;}
	else if(val == 5){changeItme = gwanwak;}
	else if(val == 6){changeItme = gwangjin;}
	else if(val == 7){changeItme = guro;}
	else if(val == 8){changeItme = geumcheon;}
	else if(val == 9){changeItme = nowon;}
	else if(val == 10){changeItme = dobong;}
	else if(val == 11){changeItme = dongdaemoon;}
	else if(val == 12){changeItme = dongjak;}
	else if(val == 13){changeItme = Mapo;}
	else if(val == 14){changeItme = seodaemon;}
	else if(val == 15){changeItme = seocho;}
	else if(val == 16){changeItme = seongdong;}
	else if(val == 17){changeItme = seongbuk;}
	else if(val == 18){changeItme = songpa;}
	else if(val == 19){changeItme = yangcheon;}
	else if(val == 20){changeItme = yeongdeunpo;}
	else if(val == 21){changeItme = yongsan;}
	else if(val == 22){changeItme = eunpyeong;}
	else if(val == 23){changeItme = jongro;}
	else if(val == 24){changeItme = jung;}
	else if(val == 25){changeItme = jungang;}
	
	
	
	$('#DongID').empty();
	for(var count = 0; count < changeItme.length; count++){ 
                var option = $("<option>"+changeItme[count]+"</option>"); // Dong에 gangnam을 입력함.
                $('#DongID').append(option);
		
            }

	

}