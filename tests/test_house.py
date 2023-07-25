import claritygov.services.legislators_service as legislators_service

json = legislators_service.get_state_house_members('md')
print(json)