import cloudgenix

AUTH_TOKEN='EnterAuth Token'

#Instantiate Cloudgenix API object
cgx_session1 = cloudgenix.API("https://api.elcapitan.cloudgenix.com", ssl_verify=False)
cgx_session1.interactive.use_token(AUTH_TOKEN)

####Get the Site List Config
GET_Sites = cgx_session1.get.sites()

if GET_Sites.cgx_status:
    sitelist = GET_Sites.cgx_content.get("items", None)
    for site in sitelist:
        if site["security_policysetstack_id"] == None and site["element_cluster_role"] == "SPOKE":
            print (site["name"], site["security_policysetstack_id"])
