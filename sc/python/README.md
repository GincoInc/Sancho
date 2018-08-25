- deploy()
```
OWNERにSanchoTokenを発行
return bool
```

- claimTokens()
```
return claim_tokens(ctx)
```
- vote(投票する書籍のhash,著者に推薦するアドレス)
```
return bool
```

- getVote(投票状況を参照したい書籍のhash)
```
投票状況の一覧
return bytearray
```

- getData()
```
書籍一覧の参照
return bytearray
```

- putData(書籍データ)
```
書籍の登録
return bool
```

- deleteData()
```
書籍DBの削除
return bool
```

- withdraw()
```
voteされたaddressのユーザー自身が叩いた時にそのユーザー宛てにOWNERからSanchoTokenが送付される
return bool
```
