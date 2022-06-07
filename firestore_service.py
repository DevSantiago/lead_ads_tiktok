from google.cloud import firestore
import google.auth


class Firestore:
    def __init__(self):
        self.credentials, project = google.auth.default()
        self.db = firestore.Client()

    def set(self, lead_data):
        self.lead_data =  lead_data
        self.data = ({
            u'customer': u'camper',
            u'created_at': self.lead_data['data']['meta_data']['create_time'],
            u'sent_to_crm': False
         })

        try:
            self.db.collection('tiktokLeadAdsCustomers-dev').document(str(self.lead_data['data']['meta_data']['lead_id'])).set(self.data)

            return "The record has been successfully registered in Firestore"
        except ValueError:
            return ValueError('Something happened while entering the log in Firestore')


    def update(self, lead_data):
        self.lead_data = lead_data['data']['meta_data']['lead_id']

        try:
            document = self.db.collection(u'tiktokLeadAdsCustomers-dev').document(str(self.lead_data))
            document.update({'sent_to_crm': True})

            return "The record has been successfully updated in Firestore"
        except ValueError(E):
            return "Something happened while updating the registry in Firestore"
