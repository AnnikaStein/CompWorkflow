# PostComp

---

## Mail only those who actually attended
__Command__
```shell
python -m CompWorkflow.PostComp.aftercompMail -c mzc25.yml --debug
```

__Requirements__
- needs WCIF (post comp) to proceed
- needs survey link in config to proceed
- needs participant cert drive link in config to proceed

__Outputs__  
inside /output/<compID> there will be
- mail_aftercomp_recipients.txt (contains all emails, semicolon-separated to insert into mail program)
- mail_aftercomp.txt (content of the mail in German and English)
- participants/participant_cert_*.tex/*.pdf (participant certificates, tex source and compiled pdf)
