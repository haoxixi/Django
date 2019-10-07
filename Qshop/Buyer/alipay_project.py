from alipay import AliPay

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0/x9pVL5lA8qre5VuYMJpgNQX2XAdkuou/nAT5Rf5mAJocI73gVgTXhPOTyp4qXiUTyvGa0jo7HPMoHEmfIquvMJWeOnoj4wlhyqEvjTst2l6GdLg6/dPJBxT9wQSZxSpOsi+DH8G4Z7p9NPkCcSfIHTmgPdVuOCvgemvbl+9jgkf3blz1jvc5Zj+VGIVAigsCD8ryC2waPMIE9WQe54kKnIVmda7+cbxfMstSJKEZgD1e5LjNF6Xu7xBmXIq+XJrhKgFBq/EoK1No+F/Tr4j9/g3zhKVm07UsngDcQN2AnPViqyFgjAlfU4MpeKzxGgF6xJ/k0Hs+kzmuSyuUB24wIDAQAB
-----END PUBLIC KEY-----"""

alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0/x9pVL5lA8qre5VuYMJpgNQX2XAdkuou/nAT5Rf5mAJocI73gVgTXhPOTyp4qXiUTyvGa0jo7HPMoHEmfIquvMJWeOnoj4wlhyqEvjTst2l6GdLg6/dPJBxT9wQSZxSpOsi+DH8G4Z7p9NPkCcSfIHTmgPdVuOCvgemvbl+9jgkf3blz1jvc5Zj+VGIVAigsCD8ryC2waPMIE9WQe54kKnIVmda7+cbxfMstSJKEZgD1e5LjNF6Xu7xBmXIq+XJrhKgFBq/EoK1No+F/Tr4j9/g3zhKVm07UsngDcQN2AnPViqyFgjAlfU4MpeKzxGgF6xJ/k0Hs+kzmuSyuUB24wIDAQABAoIBAGXHsuPvxNjrt0gvSIV7fuRwbuR+zDt/9BHcxhLvYGQR9E3wHiJpXmWTwCXxFHg3wUPT6RZg5N2xf5P2blijxxRfoDvCbDgft+A6/wWA5tPYS9Ib1kvx4j0z9NOtCzzsi1mXdADKrwrgNPrNIERMHjodc2VdOaaAMcPflJU/PNAmIBW7rGsFONcLFb4fkE8CbD8/uAaOmNLIGpkO95HDeXyHGW19S76PTJ+bXJQeNdewsHrggkJuqres7ZP7NrmYod78q35CCh1BHlAOic5KNeguPBTvQqGXcDuoTqhX3xKsOAvb83HOKoIZHinKWZ5eIHbfNCZ3f5k14eKZVTEYb5ECgYEA/TWDufqTMi+vnb3inBd1Ow+nYmU69HPf5NluydzZYvM+Skmrih8jhwHl4mF0GKcE0Ce9bm/98s+y4B9oH3vHL2hjWczoegUSy1lxaDOnsxT2E7soDPAO6Pt5PBNfotgHQUrP2WVbi3X5wosS3HBxHEYtFucioTbWJW68Jx89Ym8CgYEA1lKoOSsMCJFWmii13PghuuibY2cND05DGmBUULR2cW9mNFnnVP2EuxgcWzRmb5c0F+iQqUe148R6XAluZoypNTZ7j0fqhojtlQOwxdVCEypV5BcqW/Ns//+Kvl1/cyGh+juubDW3PpfCknrp8ZTcslBzNyUQerEp8MQTZN8znM0CgYA+4k94nLZ5vEYNEt94jIrcxCJ52VIu66grGaTeFS8X1/kcUfd8MgeMu/fvpOxEQxZ666OsDbwv1U1DRAmD6CWrrG0gHDeQNjpYrjnv+wQnAYmrlMt5ixTo36tYNCeINcZ3fLDp+LYniIEiw49Hl9U/hF4mVfjPuOKuITYxMRz5mQKBgQCb4HgrRAy3eoVDD9LdiLZ3i0/gpwWPmTsixubr36S5ce0irDSc0tojfTC6gMzz4kPoE6SLCfXXV4IqyE08VpeGdT6+ge6ntJUfKRT7fdRVvhfEEbkkMVKYihItzDCy2sZFCf0dBKBm7Nd909msc7lkEzEI7XMj2RCI5QK5/cA7DQKBgQCYtMvXk9dRvL0kGzz1Mdr/FUQugTEHuDC8KbC9YGPVh67jMG5AKuEaQxAoZME0PT9b+ifEdFavLoDz0bJrVMHmVL9ZW8l2peT6NAxcrcenHMGxG3ot/Q+SttLYrTaBSgP0+EHlPsDKXmgMYeBtop/rh7TOfPMcCvRemVZwOq+O8A==
-----END RSA PRIVATE KEY-----"""

alipay = AliPay(
    appid = "2016101200667719",
    app_notify_url = None,
    app_private_key_string = alipay_private_key_string,
    alipay_public_key_string = alipay_public_key_string,
    sign_type = "RSA2"
)

order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no = "1000000003", #订单号
    total_amount = str(1000000),#支付金额，是字符串
    subject = "小型直升飞机家庭版", #支付主题
    return_url = None,
    notify_url = None
)#网页支付订单

result = "https://openapi.alipaydev.com/gateway.do?"+order_string

print(result)