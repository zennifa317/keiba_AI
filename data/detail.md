# About Dataset

## コンテキスト/Context
このデータセットは、JRA日本中央競馬会のレース結果、オッズ、ラップタイム、コーナー通過順位で構成されております。
データは https://www.netkeiba.com/ からスクレイピングされたもので、NaN値は除外されていないです。
データは日本語で、主に日本語を理解できる人を対象としております。
各列の英訳についても併記します。
This dataset contains JRA historic horse racing results, betting odds, lap times and corner passing orders.
The data was scraped from https://www.netkeiba.com/ and NaN values are not excluded.
The data is in Japanese and is intended primarily for people who understand Japanese,
but English translations of each column are also provided.

## コンテント/Content
### <19860105-20210731_race_result.csv>

- レース馬番ID/Race PP ID: 下記参照/See below
- レースID/Race ID: 下記参照/See below
- レース日付/Race Day
- 開催回数/Race Meeting Number
- 競馬場コード/Racecourse Code
- 競馬場名/Racecourse Name
- 開催日数/N-th Racing Day
- 競争条件/Race Condition: レースのクラス分け/Race Classifications: https://www.jra.go.jp/keiba/rules/class.html (日本語/Japanese)
- レース記号/[抽]/Race Symbol/Drawing
- レース記号/(馬齢)/Race Symbol/Age
- レース記号/牝/Race Symbol/Mare: 牝馬に限定するレース記号
- レース記号/(父)/Race Symbol/Sire: 内国産種牡馬の産駒で(マル外)以外の馬
- レース記号/(別定)/Race Symbol/Special Weight
- レース記号/(混)/Race Symbol/Mixed: 内国産馬に加えて(マル外)が出走できる競走
- レース記号/(ハンデ)/Race Symbol/Handicap: ハンデキャップ: https://www.jra.go.jp/kouza/yougo/w340.html (日本語/Japanese)
- レース記号/(抽)/Race Symbol/Drawing: ＪＲＡが市場で購入し平成１４年以前に抽選配付したサラブレッド系の内国産馬
- レース記号/(市)/Race Symbol/Market: 市場取引馬
- レース記号/(定量)/Race Symbol/Fixed Weight: 定量: https://www.jra.go.jp/kouza/yougo/w542.html (日本語/Japanese)
- レース記号/牡/Race Symbol/Stallion: 牡馬に限定するレース記号
- レース記号/関東配布馬/Race Symbol/Kanto Distributed Horses
- レース記号/(指)/Race Symbol/Specified: 地方競馬の馬および騎手が出場できる競走
- レース記号/関西配布馬/Race Symbol/Kasai Distributed Horses
- レース記号/九州産馬/Race Symbol/Horses from Kyushu
- レース記号/見習騎手/Race Symbol/Apprentice
- レース記号/せん/Race Symbol/Gelding: セン馬に限定するレース記号
- レース記号/(国際)/Race Symbol/International: 内国産馬に加えて(マル外)および[カク外]が出走できる競走
- レース記号/[指]/Race Symbol/Specified: 地方競馬の騎手が騎乗できる競走
- レース記号/(特指)/Race Symbol/Special Specified: ＪＲＡが認定した地方競馬の競走または競馬番組で別に定める地方競馬の競走で第１着となった[カク地]が出走できまた地方競馬の騎手が騎乗できる競走
- レース番号/Race Number
- 重賞回次/Graded Races N-th Time
- レース名/Race Name
- リステッド・重賞競走/ Listed and Graded Races
- 障害区分/Steeplechase Category
- 芝・ダート区分/Turf and Dirt Category
- 芝・ダート区分2/Turf and Dirt Category2: 障害レースで芝とダートの両方を利用するケース有り/There are cases where both turf and dirt are used for steeplechase.
- 右左回り・直線区分/Clockwise, Anti-clockwise and Straight Course Category
- 内・外・襷区分/Inner Circle, Outer Circle and Tasuki Course Category: 障害レースで用いられる襷コースは現在は廃止/The Tasuki(crossing the course at an angle) course used in steeplechase is now obsolete.
- 距離(m)/Distance(m)
- 天候/Weather
- 馬場状態1/Track Condition1
- 馬場状態2/Track Condition2: 障害レースで芝とダートの両方を利用するケース有り/There are cases where both turf and dirt are used for steeplechase.
- 発走時刻/Post Time
- 着順/FP: Final Position: 失格、取消、除外、中断の場合は空白で着順注記に明記/In the case of Disqualified,Excluded from running, Scratched and Fail to finish, leave NaN and specify the reason in 着順注記/FP Note.
- 着順注記/FP Note: 降着(降)、再騎乗(再)、失格(失)、取消(取)、除外(除)、中断(中)を注記
- 枠番/BK: Bracket Number
- 馬番/PP: Post Position
- 馬名/Horse Name
- 性別/Sex
- 馬齢/Age
- 斤量/Weight(Kg)
- 騎手/Jockey
- タイム/Total Time(1/10s)
- 着差/Margin
- 1コーナー/Position 1st Corner: 第1コーナーを通過した順位を馬番で表示/Show the order in which the horse passed the 1st corner by the post position(PP).
- 2コーナー/Position 2nd Corner: 第2コーナーを通過した順位を馬番で表示/Show the order in which the horse passed the 2nd corner by the PP.
- 3コーナー/Position 3rd Corner: 第3コーナーを通過した順位を馬番で表示/Show the order in which the horse passed the 3rd corner by the PP.
- 4コーナー/Position 4th Corner: 第4コーナーを通過した順位を馬番で表示/Show the order in which the horse passed the 4th corner by the PP.
- 上り/L3F: Time of Last 3 Furlongs (600m)
- 単勝/Win Odds(100Yen)
- 人気/Win Fav: FAVはFavoriteの略/FAV stands for Favorite.
- 馬体重/Horse Weight: 馬体重計その他の事故によって、計量不能となった場合は省略/Cases in which weighing is not possible due to an accident with the scales or other equipment are omitted(NaN).
- 場体重増減/Horse Weight Gain and Loss: 前走時の馬体重との差/Difference from the horse's weight at the previous race
- 東西・外国・地方区分/East, West, Foreign Country and Local Category
- 調教師/Trainer
- 馬主/Owner
- 賞金(万円)/Prize Money(10000Yen)

| レースID/Race ID | 列/Column | 列説明/Column Description |
|-|-|-|
| 1桁目/1st Digit | レース日付/Race Day | 西暦1桁目/1st Digit of the Year |
| 2桁目/2nd Digit | レース日付/Race Day | 西暦2桁目/2nd Digit of the Year |
| 3桁目/3rd Digit | レース日付/Race Day | 西暦3桁目/3rd Digit of the Year |
| 4桁目/4th Digit | レース日付/Race Day | 西暦4桁目/4th Digit of the Year |
| 5桁目/5th Digit | 競馬場コード/Racecourse Code | 1桁目/1st Digit *Note1 |
| 6桁目/6th Digit | 競馬場コード/Racecourse Code | 2桁目/2nd Digit |
| 7桁目/7th Digit | 開催回数/Race Meeting Number | 1桁目/1st Digit *Note1 |
| 8桁目/8th Digit | 開催回数/Race Meeting Number | 2桁目/2nd Digit | 
| 9桁目/9th Digit | 開催日数/N-th Racing Day | 1桁目/1st Digit *Note1 |
| 10桁目/10th Digit | 開催日数/N-th Racing Day | 2桁目/2nd Digit |
| 11桁目/11th Digit | レース番号/Race Number | 1桁目/1st Digit *Note1 |
| 12桁目/12th Digit | レース番号/Race Number | 2桁目/2nd Digit |

Note1: 各列1桁の場合は、ゼロ埋め/In the case of a single digit in each column, fill in with zero.
Note2: "https://db.netkeiba.com/race/レースID/"でスクレイピングURLにアクセス可能
Note2: Scraping URL can be accessed at "ht>tps://db.netkeiba.com/race/RaceIDColumn/".
Note3: レース馬番IDは、レースIDの13・14桁目に馬番を付したID
Note3: Race PP ID is the ID with the PP column attached to the 13th and 14th digits of the Race ID.

リファレンス/Reference
馬やレースに付く記号/Symbols attached to horses and races: https://www.jra.go.jp/keiba/rules/ (日本語/Japanese)
成績表の見方/How to Read Race Result: https://www.jra.go.jp/datafile/seiseki/report/mikata3.html (日本語/Japanese)
Wikipedia競馬場/Racecourse : https://ja.wikipedia.org/wiki/%E7%AB%B6%E9%A6%AC%E5%A0%B4 (日本語/Japanese)
JRA Race Card & Results: https://jra.jp/JRAEN/AP/common/main (英語/English)

### <19860105-20210731_odds.csv>

- レースID/Race ID: race_resultファイルのレースIDの外部キー/foreign key for the race_result Race ID column.
- 単勝1_馬番/Win1_PP: 単勝式馬券の馬番
- 単勝2_馬番/Win2_PP: 単勝式馬券の馬番 ※1着2頭同着時に発生/Occurs when 2 horses are tied for 1st place
- 単勝1_オッズ/Win1_Odds:単勝式馬券のオッズ(円/Yen)
- 単勝2_オッズ/Win2_Odds: 単勝式馬券のオッズ(円/Yen)
- 単勝1_人気/Win1_Fav: 単勝式馬券の人気
- 単勝2_人気/Win2_Fav: 単勝式馬券の人気
- 複勝1_馬番/Place1_PP: 複勝式馬券の馬番
- 複勝2_馬番/Place2_PP: 複勝式馬券の馬番
- 複勝3_馬番/Place3_PP: 複勝式馬券の馬番
- 複勝4_馬番/Place4_PP: 複勝式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- 複勝5_馬番/Place5_PP: 複勝式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- 複勝1_オッズ/Place1_Odds: 複勝式馬券のオッズ(円/Yen)
- 複勝2_オッズ/Place2_Odds: 複勝式馬券のオッズ(円/Yen)
- 複勝3_オッズ/Place3_Odds: 複勝式馬券のオッズ(円/Yen)
- 複勝4_オッズ/Place4_Odds: 複勝式馬券のオッズ(円/Yen)
- 複勝5_オッズ/Place5_Odds: 複勝式馬券のオッズ(円/Yen)
- 複勝1_人気/Place1_Fav: 複勝式馬券の人気
- 複勝2_人気/Place2_Fav: 複勝式馬券の人気
- 複勝3_人気/Place3_Fav: 複勝式馬券の人気
- 複勝4_人気/Place4_Fav: 複勝式馬券の人気
- 複勝5_人気/Place5_Fav: 複勝式馬券の人気
- 枠連1_組合せ1/Bracket Quinella1_Permutation1: 枠番号二連勝複式馬券の馬番
- 枠連1_組合せ2/Bracket Quinella1_Permutation2: 枠番号二連勝複式馬券の馬番
- 枠連2_組合せ1/Bracket Quinella2_Permutation1: 枠番号二連勝複式馬券の馬番 ※2着2頭同着時に発生/Occurs when 2 horses are tied for 1st place
- 枠連2_組合せ2/Bracket Quinella2_Permutation2: 枠番号二連勝複式馬券の馬番 ※2着2頭同着時に発生/Occurs when 2 horses are tied for 1st place
- 枠連1_オッズ/Bracket Quinella1_Odds: 枠番号二連勝複式馬券のオッズ(円/Yen)
- 枠連2_オッズ/Bracket Quinella2_Odds: 枠番号二連勝複式馬券のオッズ(円/Yen)
- 枠連1_人気/Bracket Quinella1_Fav: 枠番号二連勝複式馬券の人気
- 枠連2_人気/Bracket Quinella2_Fav: 枠番号二連勝複式馬券の人気
- 馬連1_組合せ1/Quinella1_Permutation1: 普通馬番号二連勝複式馬券の馬番
- 馬連1_組合せ2/Quinella1_Permutation2: 普通馬番号二連勝複式馬券の馬番
- 馬連2_組合せ1/Quinella2_Permutation1: 普通馬番号二連勝複式馬券の馬番 ※2着2頭同着時に発生/Occurs when 2 horses are tied for 2nd place
- 馬連2_組合せ2/Quinella2_Permutation2: 普通馬番号二連勝複式馬券の馬番 ※2着2頭同着時に発生/Occurs when 2 horses are tied for 2nd place
- 馬連1_オッズ/Quinella1_Odds: 普通馬番号二連勝複式馬券のオッズ(円/Yen)
- 馬連2_オッズ/Quinella2_Odds: 普通馬番号二連勝複式馬券のオッズ(円/Yen)
- 馬連1_人気/Quinella1_Fav: 普通馬番号二連勝複式馬券の人気
- 馬連2_人気/Quinella2_Fav: 普通馬番号二連勝複式馬券の人気
- ワイド1_組合せ1/Quinella Place1_Permutation1: 拡大馬番号二連勝複式馬券の馬番
- ワイド1_組合せ2/Quinella Place1_Permutation2: 拡大馬番号二連勝複式馬券の馬番
- ワイド2_組合せ1/Quinella Place2_Permutation1: 拡大馬番号二連勝複式馬券の馬番
- ワイド2_組合せ2/Quinella Place2_Permutation2: 拡大馬番号二連勝複式馬券の馬番
- ワイド3_組合せ1/Quinella Place3_Permutation1: 拡大馬番号二連勝複式馬券の馬番
- ワイド3_組合せ2/Quinella Place3_Permutation2: 拡大馬番号二連勝複式馬券の馬番
- ワイド4_組合せ1/Quinella Place4_Permutation1: 拡大馬番号二連勝複式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- ワイド4_組合せ2/Quinella Place4_Permutation2: 拡大馬番号二連勝複式馬券の馬番※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- ワイド5_組合せ1/Quinella Place5_Permutation1: 拡大馬番号二連勝複式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- ワイド5_組合せ2/Quinella Place5_Permutation2: 拡大馬番号二連勝複式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- ワイド6_組合せ1/Quinella Place6_Permutation1: 拡大馬番号二連勝複式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- ワイド6_組合せ2/Quinella Place6_Permutation2: 拡大馬番号二連勝複式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- ワイド7_組合せ1/Quinella Place7_Permutation1: 拡大馬番号二連勝複式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- ワイド7_組合せ2/Quinella Place7_Permutation2: 拡大馬番号二連勝複式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- ワイド1_オッズ/Quinella Place1_Odds: 拡大馬番号二連勝複式馬券のオッズ(円/Yen)
- ワイド2_オッズ/Quinella Place2_Odds: 拡大馬番号二連勝複式馬券のオッズ(円/Yen)
- ワイド3_オッズ/Quinella Place3_Odds: 拡大馬番号二連勝複式馬券のオッズ(円/Yen)
- ワイド4_オッズ/Quinella Place4_Odds: 拡大馬番号二連勝複式馬券のオッズ(円/Yen)
- ワイド5_オッズ/Quinella Place5_Odds: 拡大馬番号二連勝複式馬券のオッズ(円/Yen)
- ワイド6_オッズ/Quinella Place6_Odds: 拡大馬番号二連勝複式馬券のオッズ(円/Yen)
- ワイド7_オッズ/Quinella Place7_Odds: 拡大馬番号二連勝複式馬券のオッズ(円/Yen)
- ワイド1_人気/Quinella Place1_Fav: 拡大馬番号二連勝複式馬券の人気
- ワイド2_人気/Quinella Place2_Fav: 拡大馬番号二連勝複式馬券の人気
- ワイド3_人気/Quinella Place3_Fav: 拡大馬番号二連勝複式馬券の人気
- ワイド4_人気/Quinella Place4_Fav: 拡大馬番号二連勝複式馬券の人気
- ワイド5_人気/Quinella Place5_Fav: 拡大馬番号二連勝複式馬券の人気
- ワイド6_人気/Quinella Place6_Fav: 拡大馬番号二連勝複式馬券の人気
- ワイド7_人気/Quinella Place7_Fav: 拡大馬番号二連勝複式馬券の人気
- 馬単1_組合せ1/Exacta1_Exact Order1: 馬番号二連勝単式馬券の馬番
- 馬単1_組合せ2/Exacta1_Exact Order2: 馬番号二連勝単式馬券の馬番
- 馬単2_組合せ1/Exacta2_Exact Order1: 馬番号二連勝単式馬券の馬番 ※1着2頭同着か2着2頭同着時に発生/Occurs when 2 horses are tied for 1st place or 2 horses are tied for 2nd place
- 馬単2_組合せ2/Exacta2_Exact Order2: 馬番号二連勝単式馬券の馬番 ※1着2頭同着か2着2頭同着時に発生/Occurs when 2 horses are tied for 1st place or 2 horses are tied for 2nd place
- 馬単1_オッズ/Exacta1_Odds: 馬番号二連勝単式馬券のオッズ(円/Yen)
- 馬単2_オッズ/Exacta2_Odds: 馬番号二連勝単式馬券のオッズ(円/Yen)
- 馬単1_人気/Exacta1_Fav: 馬番号二連勝単式馬券の人気
- 馬単2_人気/Exacta2_Fav: 馬番号二連勝単式馬券の人気
- 三連複1_組合せ1/Trio1_Permutation1: 馬番号三連勝複式馬券の馬番
- 三連複1_組合せ2/Trio1_Permutation2: 馬番号三連勝複式馬券の馬番
- 三連複1_組合せ3/Trio1_Permutation3: 馬番号三連勝複式馬券の馬番
- 三連複2_組合せ1/Trio2_Permutation1: 馬番号三連勝複式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- 三連複2_組合せ2/Trio2_Permutation2: 馬番号三連勝複式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- 三連複2_組合せ3/Trio2_Permutation3: 馬番号三連勝複式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- 三連複3_組合せ1/Trio3_Permutation1: 馬番号三連勝複式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- 三連複3_組合せ2/Trio3_Permutation2: 馬番号三連勝複式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- 三連複3_組合せ3/Trio3_Permutation3: 馬番号三連勝複式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- 三連複1_オッズ/Trio1_Odds: 馬番号三連勝複式馬券のオッズ(円/Yen)
- 三連複2_オッズ/Trio2_Odds: 馬番号三連勝複式馬券のオッズ(円/Yen)
- 三連複3_オッズ/Trio3_Odds: 馬番号三連勝複式馬券のオッズ(円/Yen)
- 三連複1_人気/Trio1_Fav: 馬番号三連勝複式馬券の人気
- 三連複2_人気/Trio2_Fav: 馬番号三連勝複式馬券の人気
- 三連複3_人気/Trio3_Fav: 馬番号三連勝複式馬券の人気
- 三連単1_組合せ1/Trifecta1_Exact Order1: 馬番号三連勝単式馬券の馬番
- 三連単1_組合せ2/Trifecta1_Exact Order2: 馬番号三連勝単式馬券の馬番
- 三連単1_組合せ3/Trifecta1_Exact Order3: 馬番号三連勝単式馬券の馬番
- 三連単2_組合せ1/Trifecta2_Exact Order1: 馬番号三連勝単式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- 三連単2_組合せ2/Trifecta2_Exact Order2: 馬番号三連勝単式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- 三連単2_組合せ3/Trifecta2_Exact Order3: 馬番号三連勝単式馬券の馬番 ※3着2・3頭同着時に発生/Occurs when 2 or 3 horses are tied for 3rd place
- 三連単3_組合せ1/Trifecta3_Exact Order1: 馬番号三連勝単式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- 三連単3_組合せ2/Trifecta3_Exact Order2: 馬番号三連勝単式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- 三連単3_組合せ3/Trifecta3_Exact Order3: 馬番号三連勝単式馬券の馬番 ※3着3頭同着時に発生/Occurs when 3 horses are tied for 3rd place
- 三連単1_オッズ/Trifecta1_Odds: 馬番号三連勝単式馬券のオッズ(円/Yen)
- 三連単2_オッズ/Trifecta2_Odds: 馬番号三連勝単式馬券のオッズ(円/Yen)
- 三連単3_オッズ/Trifecta3_Odds: 馬番号三連勝単式馬券のオッズ(円/Yen)
- 三連単1_人気/Trifecta1_Fav: 馬番号三連勝単式馬券の人気
- 三連単2_人気/Trifecta2_Fav: 馬番号三連勝単式馬券の人気
- 三連単3_人気/Trifecta3_Fav: 馬番号三連勝単式馬券の人気

リファレンス/Reference
単勝/Win: https://www.jra.go.jp/kouza/yougo/w423.html (日本語/Japanese)
複勝/Place: https://www.jra.go.jp/kouza/yougo/w432.html (日本語/Japanese)
枠連/Bracket Quinella: https://www.jra.go.jp/kouza/yougo/w529.html (日本語/Japanese)
馬連/Quinella: https://www.jra.go.jp/kouza/yougo/w530.html (日本語/Japanese)
ワイド/Quinella Place: https://www.jra.go.jp/kouza/yougo/w524.html (日本語/Japanese)
馬単/Exacta: https://www.jra.go.jp/kouza/yougo/w531.html (日本語/Japanese)
三連複/Trio: https://www.jra.go.jp/kouza/yougo/w532.html (日本語/Japanese)
三連単/Trifecta: https://www.jra.go.jp/kouza/yougo/w533.html (日本語/Japanese)
馬券の種類/Type of Betting: https://www.jra.go.jp/kouza/beginner/baken/ (日本語/Japanese)

For those of you who don't understand Japanese, the following document has been compiled by JRA.
How to Bet: https://japanracing.jp/en/racing/go_racing/pdf/how_to_bet_en.pdf (English)

### <19860105-20210731_laptime.csv>

ラップタイムN-thは、各地点間の時間を表す/Lap time N-th represents the time between each point(1/10s)
ペースN-thは、各地点間の累積時間を表す/Pace Time N-th represents the cumulative time between each point(1/10s)

- レースID/Race ID: race_resultファイルのレースIDの外部キー/foreign key for the race_result Race ID column.
- ラップタイム1/Lap Time 1: 偶数の距離/Even Number Distance(0m-200m)、奇数の距離/Odd Number Distance(0m-100m)
- ラップタイム2/Lap Time 2: 偶数の距離/Even Number Distance(200m-400m)、奇数の距離/Odd Number Distance(100m-300m)
- ラップタイム3/Lap Time 3: 偶数の距離/Even Number Distance(400m-600m)、奇数の距離/Odd Number Distance(300m-500m)
- ラップタイム4/Lap Time 4: 偶数の距離/Even Number Distance(600m-800m)、奇数の距離/Odd Number Distance(500m-700m)
- ラップタイム5/Lap Time 5: 偶数の距離/Even Number Distance(800m-1000m)、奇数の距離/Odd Number Distance(700m-900m)
- ラップタイム6/Lap Time 6: 偶数の距離/Even Number Distance(1000m-1200m)、奇数の距離/Odd Number Distance(900m-1100m)
- ラップタイム7/Lap Time 7: 偶数の距離/Even Number Distance(1200m-1400m)、奇数の距離/Odd Number Distance(1100m-1300m)
- ラップタイム8/Lap Time 8: 偶数の距離/Even Number Distance(1400m-1600m)、奇数の距離/Odd Number Distance(1300m-1500m)
- ラップタイム9/Lap Time 9: 偶数の距離/Even Number Distance(1600m-1800m)、奇数の距離/Odd Number Distance(1500m-1700m)
- ラップタイム10/Lap Time 10: 偶数の距離/Even Number Distance(1800m-2000m)、奇数の距離/Odd Number Distance(1700m-1900m)
- ラップタイム11/Lap Time 11: 偶数の距離/Even Number Distance(2000m-2200m)、奇数の距離/Odd Number Distance(1900m-2100m)
- ラップタイム12/Lap Time 12: 偶数の距離/Even Number Distance(2200m-2400m)、奇数の距離/Odd Number Distance(2100m-2300m)
- ラップタイム13/Lap Time 13: 偶数の距離/Even Number Distance(2400m-2600m)、奇数の距離/Odd Number Distance(2300m-2500m)
- ラップタイム14/Lap Time 14: 偶数の距離/Even Number Distance(2600m-2800m)
- ラップタイム15/Lap Time 15: 偶数の距離/Even Number Distance(2800m-3000m)
- ラップタイム16/Lap Time 16: 偶数の距離/Even Number Distance(3000m-3200m)
- ラップタイム17/Lap Time 17: 偶数の距離/Even Number Distance(3200m-3400m)
- ラップタイム18/Lap Time 18: 偶数の距離/Even Number Distance(3400m-3600m)
- ペース1/Pace Time 1: 偶数の距離/Even Number Distance(0m-200m)、奇数の距離/Odd Number Distance(0m-100m)
- ペース2/Pace Time 2: 偶数の距離/Even Number Distance(0m-400m)、奇数の距離/Odd Number Distance(0m-300m)
- ペース3/Pace Time 3: 偶数の距離/Even Number Distance(0m-600m)、奇数の距離/Odd Number Distance(0m-500m)
- ペース4/Pace Time 4: 偶数の距離/Even Number Distance(0m-800m)、奇数の距離/Odd Number Distance(0m-700m)
- ペース5/Pace Time 5: 偶数の距離/Even Number Distance(0m-1000m)、奇数の距離/Odd Number Distance(0m-900m)
- ペース6/Pace Time 6: 偶数の距離/Even Number Distance(0m-1200m)、奇数の距離/Odd Number Distance(0m-1100m)
- ペース7/Pace Time 7: 偶数の距離/Even Number Distance(0m-1400m)、奇数の距離/Odd Number Distance(0m-1300m)
- ペース8/Pace Time 8: 偶数の距離/Even Number Distance(0m-1600m)、奇数の距離/Odd Number Distance(0m-1500m)
- ペース9/Pace Time 9: 偶数の距離/Even Number Distance(0m-1800m)、奇数の距離/Odd Number Distance(0m-1700m)
- ペース10/Pace Time 10: 偶数の距離/Even Number Distance(0m-2000m)、奇数の距離/Odd Number Distance(0m-1900m)
- ペース11/Pace Time 11: 偶数の距離/Even Number Distance(0m-2200m)、奇数の距離/Odd Number Distance(0m-2100m)
- ペース12/Pace Time 12: 偶数の距離/Even Number Distance(0m-2400m)、奇数の距離/Odd Number Distance(0m-2300m)
- ペース13/Pace Time 13: 偶数の距離/Even Number Distance(0m-2600m)、奇数の距離/Odd Number Distance(0m-2500m)
- ペース14/Pace Time 14: 偶数の距離/Even Number Distance(0m-2800m)
- ペース15/Pace Time 15: 偶数の距離/Even Number Distance(0m-3000m)
- ペース16/Pace Time 16: 偶数の距離/Even Number Distance(0m-3200m)
- ペース17/Pace Time 17: 偶数の距離/Even Number Distance(0m-3400m)
- ペース18/Pace Time 18: 偶数の距離/Even Number Distance(0m-3600m)
- 前半3ハロン/F3F: Time of First 3 Furlongs (600m)
- 上がり3ハロン/L3F: Time of Last 3 Furlongs (600m)

Note: "前半3ハロン/F3F", "上がり3ハロン/L3F" 詳細は不明ですが、2002年6月15日開催日より前半3ハロン/上がり3ハロンが計測されています/Details are unknown, but F3F and L3F have been measured since June 15, 2002.
リファレンス/Reference
ハロンタイム/Furlong Time: https://www.jra.go.jp/kouza/yougo/w291.html (日本語/Japanese)

### <20020615-20210731_corner_passing_order.csv>

- レースID/Race ID: race_resultファイルのレースIDの外部キー/foreign key for the race_result Race ID column.
- 1コーナー/Position 1st Corner: 第1コーナーを通過した順序を馬番で表示/Show the order in which the horses passed the 1st corner by post position(PP).
- 2コーナー/Position 2nd Corner: 第2コーナーを通過した順序を馬番で表示/Show the order in which the horses passed the 2nd corner by PP.
- 3コーナー/Position 3rd Corner: 第3コーナーを通過した順序を馬番で表示/Show the order in which the horses passed the 3rd corner by PP.
- 4コーナー/Position 4th Corner: 第4コーナーを通過した順序を馬番で表示/Show the order in which the horses passed the 4th corner by PP.

|記号/Symbol | 各馬の前後間隔を以下の記号で表示します。 | The front and rear intervals for each horse are indicated by the following symbols |
|---|---|---|
| （） | 1馬身未満の差で併走している馬群を示し、（）内は内側の馬から記します。 | Horses running together by less than one horse length are shown in parentheses, with the horses on the inside first. |
| * | 馬群の先頭馬を示します。 | The first horse in the group is indicated. |
| , |先行馬から1馬身以上2馬身未満の差を示します。 | Indicates the leader of the group of horses by more than one horse length but less than two horse lengths. |
| -	| 先行馬から2馬身以上5馬身未満の差を示します。 | Indicates a gap of 2 to 5 horse lengths from the horse in front. |
| =	| 先行馬から5馬身以上の差を示します。 | Indicates a gap of 5 lengths or more from the horse in front. |

リファレンス/Reference
レース結果の見方(記号O)/How to Read Race Result: https://www.jra.go.jp/JRADB/mikata/result.html (日本語/Japanese)

### 謝意/Acknowledgements
データは https://www.netkeiba.com/ からスクレイピングされたものです。
The data was scraped from https://www.netkeiba.com/.

### インスピレーション/Inspiration
データの使用用途の例/You can use the data to:

- 統計分析/Perform statistical analysis;
- 独自の競馬予想システムの構築/Build your own horse racing forecast system;
- Discussionトピックの特定/Identify discussion topics;

個人的に以下のような競馬格言の検証を考えております/I personally want to perform validation of the adage as followings;

- 長距離の逃げ馬/Go for the runaway horse in long-distance races.
- 短距離の差し馬/Go for the off-pace horse in short-distance races.
- 2強対決は両雄並び立たず/The two strongest horses in the race are not on par with each other.
- 夏は牝馬,牝馬は格より勢い/Summer is for mares, and mares are more momentum than their class.
- 長距離は騎手で買え/Buy by their jockeys in long-distance races.
- 逃げ馬は人気薄を狙え/Buy the underdog runaway horses.
- 2頭出しは人気薄を狙え/Buy the underdog in two horses from the same stable in a same race.
- 圧倒的１番人気の最内枠と最外枠は消し/Eliminate the overwhelmingly favorite horses in the innermost and outermost stall.