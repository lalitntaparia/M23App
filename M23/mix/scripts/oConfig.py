NEXAR_URL = "https://api.nexar.com/graphql"
QUERY_MPN = """ query ($mpn: String!) {
  supSearchMpn(q: $mpn) {
    results {
      part {
        # category {
        #   parentId
        #   id
        #   name
        #   path
        # }
        mpn
        id
        manufacturer {
          name
          id
        }
        medianPrice1000 {
          quantity
          price
          currency
        }
        estimatedFactoryLeadDays
        # extras {
        #   lifeCycle
        # }
        totalAvail
        sellers (authorizedOnly: true) {
          company {
            name
            homepageUrl
          }
          isAuthorized
          offers {
            # sku
            id
            inventoryLevel
            updated
            prices {
              price
              quantity
              currency
            }
          }
        }
        # descriptions {

        #   creditString
        # }
      }
    }
  }
}"""

QUERY_MPN_2_ORIGINAL = """ query ($mpn: String!) { 
  supSearchMpn(q: $mpn,filters: { manufacturer_id: $mpn_oct_id }) {
    hits
    results {
      part {
        # category {
        #   parentId
        #   id
        #   name
        #   path
        # }
        mpn
        id
        manufacturer {
          name
          id
        }
        medianPrice1000 {
          quantity
          price
          currency
        }
        estimatedFactoryLeadDays
        # extras {
        #   lifeCycle
        # }
        totalAvail
        sellers (authorizedOnly: true) {
          company {
            name
            homepageUrl
          }
          isAuthorized
          offers {
            # sku
            id
            inventoryLevel
            updated
            prices {
              price
              quantity
              currency
            }
          }
        }
        # descriptions {

        #   creditString
        # }
      }
    }
  }
}"""


QUERY_MPN_2 = """query ($mpn:String!) {
  supSearchMpn(q: $mpn, filters: { manufacturer_id: $mpn_oct_id }) {
    hits
    results {
      part {
        # category {
        #   parentId
        #   id
        #   name
        #   path
        # }
        mpn
        id
        manufacturer {
          name
          id
        }
        medianPrice1000 {
          quantity
          price
          currency
        }
        # estimatedFactoryLeadDays
        # extras {
        #   lifeCycle
        # }
        totalAvail
        sellers(authorizedOnly: true) {
          company {
            name
            homepageUrl
            id
          }
          isAuthorized
          offers {
            # sku
            id
            inventoryLevel
            updated
            prices {
              price
              quantity
              currency
            }
          }
        }
        # descriptions {

        #   creditString
        # }
      }
    }
  }
}
"""

top_sellers = ['Mouser',
                    'Mouser Electronics',
                    'Digi-Key',
                    'Digi-Key Marketplace',
                    'RS',
                    'RS Components - Supplier Marketing',
                    'RS Components APAC',
                    'RS Components Australia',
                    'RS Components Russia',
                    'RS Pro',
                    'RS Essentials',
                    'Farnell',
                    'Newark',
                    'Newark-in-One',
                    'element14 APAC',
                    'Avnet',
                    'Avnet Europe',
                    'Avnet Design Services',
                    'Avnet Embedded',
                    'Avnet LCD Assemblies',
                    'TTI',
                    ]