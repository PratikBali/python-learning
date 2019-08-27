'use strict';
/**
 * @ngdoc object
 * @name CONFIG
 *
 * @description
 * List of constant for every elements from backend that needs comparing or with a fixed value
 *
 **/
app.constant('CONFIG', {
  COLOR_LIST: [
    '#e74c3c',
    '#2980b9',
    '#16a085',
    '#f39c12',
    '#2c3e50',
    '#95a5a6',
    '#9b59b6',
    '#d35400',
    '#c0392b',
    '#005a88',
    '#009dc3'
  ],
  DOCUMENT_TYPE_LIST: [{
    value: 'C',
    text: 'general.documentType.CE'
  }, {
    value: 'DNI',
    text: 'general.documentType.DNI'
  }],
  DOCUMENT_TYPE_DEFAULT_VALUE: 'DNI',
  OS_TYPE: {},
  GENERIC_CODE: {
    STREET_TYPE: 'STREET_TYPE',
    HOUSING_COMPLEX_TYPE: 'HOUSING_COMPLEX_TYPE',
    DEPARTMENT: 'DEPARTMENT',
    DOCUMENT_TYPE: 'IMPL_DOCUMENT_TYPE',
    PREPAID_RECHARGE_AMOUNT: 'PREPAID_RECHARGE_AMOUNT',
    CASE_STATUS: 'IMPL_CASE_STATUS',
    CASE_CONDITION: 'IMPL_CASE_CONDITION',
    MARITAL_STATUS: 'IMPL_MARITAL_STATUS',
    INVOICE_QUERY_INPUT_CODES: 'INVOICE_QUERY_INPUT_CODES'
  },
  CATEGORY_TYPE: {
    NAVIGATION: 'NAVIGATION'
  },
  /**
   * Again MdAdil Sharukh advise to not trust strutureId and to compare names ........
   * @type {{devices: {all: string}, offers: {all: string}, superCharges: {all: string}, services: {all: string}}}
   */
  CATEGORYLIST: {
    DEVICES: 'Equipos',
    OFFERS: 'Ofertas',
    SUPERCHARGES: 'Supercargas',
    SERVICES: 'Servicios Adicionales'
  },
  FILTERLIST: {
    PACKAGE: {
      DATOS: 'Paquetes Datos',
      SMS: 'Paquetes SMS',
      MINUTOS: 'Paquetes Voz',
      MIXED: 'Paquetes Mixtos',
      FEATURED: 'Paquetes Destacados',
      ROAMING: 'Paquetes Roaming'
    },
    SUPERCHARGE: {
      DATOS: 'Supercargas Datos',
      SMS: 'Supercargas SMS',
      MINUTOS: 'Supercargas Voz',
      MIXED: 'Supercargas Mixtas',
      FEATURED: 'Ofertas Especiales'
    }
  },
  /**
   * Should be 'CHANGE' for change flow, 'NA' for the shop, 'PROVIDE' for new subscription
   */
  OPERATION: {
    NA: 'NA',
    CHANGE: 'CHANGE',
    PROVIDE: 'PROVIDE',
    PACKAGE: 'PACKAGE'
  },
  PLAN_TYPE: {
    PRE: 'PRE',
    PREPAID: 'PREPAID',
    POST: 'POST',
    POSTPAID: 'POSTPAID',
    CONTROL: 'CONTROL',
    Control: 'Control',
    BOTH: 'BOTH',
    Caribu: 'Caribu',
    CARIBU: 'CARIBU'
  },
  PAYMENT_FLOW_TYPE: {
    RECHARGE: 'R',
    PAY_BILL: 'B',
    ORDER_SUMMARY: 'P'
  },
  BUSINESS_TYPE: {
    DEVICE: 'DEVICE',
    PLAN: 'PLAN',
    OFFERING: 'OFFERING',
    PACKAGE: 'PRICE_PACKAGE',
    SERVICES: {
      FF: 'FRIENDS_AND_FAMILY',
      FF_BIS: 'Friends & Family',
      FF_TER: 'F&F',
      REGULAR: 'REGULAR'
    }
  },
  CUSTOMER_TYPE: {
    PREPAID: 'PREPAID',
    POSTPAID: 'POSTPAID',
    BOTH: 'BOTH',
    CONTROL: 'CONTROL'
  },
  UNIT: {
    MIN: 'min',
    MINUTES: 'Minutes',
    SEC: 'sec',
    SEG: 'seg',
    SECONDS: 'Seconds',
    MB: 'MB',
    GB: 'GB',
    SMS: 'SMS',
    SMS_NATIONAL: 'SMS Nacional',
    RPM: 'RPM',
    MEGABYTES: 'Megabytes'
  },
  CHARACTERISTIC_VALUE: {
    NA: 'NA',
    VOICE: 'Voz',
    DATA: 'Datos',
    SMS: 'SMS',
    RPM: 'RPM',
    RC: 'RC'
  },
  CHARACTERISTIC_VALUE_UNIT_MAPPING: {
    MIN: 'Voz',
    MINUTES: 'Voz',
    SECONDS: 'Voz',
    MB: 'Datos',
    SMS: 'SMS',
    SMS_NATIONAL: 'SMS',
    RPM: 'RPM',
    MEGABYTES: 'Datos'
  },

  LOGIN_INTERACTION_DATA: {
    CreateInteractionData: {
      interactionTitle: 'Aceptación de los términos y condiciones de Mobile app new login.',
      notes: 'Lo cliente declara ter leído y acepto en su totalidad los términos y condiciones de mobile app new login.',
      topic1: 'MobileAPP',
      topic2: 'TermsAndConditions',
      result: 'Accepted'
    }
  },

  PLAN_BALANCE_CODE: {
    POSTPAID: 'DAT1',
    CONTROL: 'DAT2',
    BAM: 'BAM2'
  },

  CHARACTERISTIC_CODE: {
    DURATION_DAYS: ['8901', '657174', '657184', '657194', '657204'],
    CODE_ASSIGNMENT: ['8881', '657134', '657144', '657154', '657164'],
    PROVISIONING_INDICATOR: ['8921', '657294', '657304', '657314', '657324'],
    PRICE: '8911',
    TYPE1: ['20664', '657254', '657264', '657274', '657284'],
    AMOUNT_DELIVER_TYPE1: ['20654', '657214', '657224', '657234', '657244'],
    SUPERCHARGE: '1248141'
  },

  PLAN_RANK_CHARACTERISTIC: '9361',

  SUPERCHARGE: {
    FALSE_EN: 'False',
    FALSE_ES: 'Falso'
  },
  DELIVERY_METHOD: {
    SIM: 'SIM',
    SIM_TYPE: 'sim',
    DEVICE_TYPE: 'device',
    CAN_STORE: 'CC',
    CAN_HOME: 'SP',
    PAPER: 'PA',
    PAPER2: 'Paper',
    EMAIL: 'EB'
  },
  STATUS: {
    SUBMITTED: 'SUBMITTED',
    CLOSED: 'CLOSED',
    VALIDATION_FAILED: 'VALIDATION_FAILED',
    ERROR: 'ERROR',
    WARNING_REFUSED: 'WARNING_REFUSED',
    NOT_FOUND: 'NOT_FOUND',
    PENDING_ORDER: 'PENDING_ORDER',
    CART_EXISTS: 'CART_EXISTS',
    INSUFFICIENT_BALANCE: 'INSUFFICIENT_BALANCE',
    LOGIN_REFUSED: 'LOGIN_REFUSED',
    LOGIN_NO_MATCH: 'LOGIN_NO_MATCH',
    WRONG_CREDENTIALS: 'WRONG_CREDENTIALS',
    USER_LOCKED: 'USER_LOCKED',
    DNI_DONOT_EXISTS: 'DNI_DONOT_EXISTS'
  },
  USAGE_TYPE: {
    SMS: 'MESSAGING',
    MESSAGE: 'MESSAGE',
    VOICE: 'VOICE',
    DATA: 'DATA',
    LOCAL: 'LOCAL',
    INTERNATIONAL: 'INTERNATIONAL'
  },
  SHOPPING_CART_ACTION: {
    ADD: 'ADD',
    REMOVE: 'REMOVE',
    CHANGE: 'CHANGE',
    NONE: 'NONE',
    None: 'None'
  },
  FLOW_TYPE: {
    BUY: 'BUY',
    CHANGE: 'CHANGE',
    FILTERED: 'FILTERED'
  },
  SERVICE_STATUS: {
    REMOVE: 'REMOVE',
    PROPOSED: 'PROPOSED',
    ACTIVE: 'ACTIVE'
  },
  SERVICES_COMP_ID: {
    DATA: '5471',
    VOICE: '5221',
    SMS: '6221'
  },
  CAMPAIGN_TYPE: {
    SUPERCHARGE: 'SCRG',
    PLAN: 'MIG',
    PACKAGE: 'PAQ',
    PROMO: 'PROMO'
  },
  CAMPAIGN_ID: {
    TEST_DRIVE_INVITE: 'TEST_DRIVE_INV_E',
    TEST_DRIVE_CHANGE_PLAN: 'TEST_DRIVE_',
    TEST_DRIVE_CLOSE: 'TESTDRIVESINOFERTA'
  },
  CAMPAIGN_ADDITIONAL: {
    ADDITINAL_USAGE: 'MBCONSTESTDRIVE',
    CAMPAIGN_START_DATE: 'FECHAINICIOCAMPANA',
    CAMPAIGN_END_DATE: 'FECHAFINCAMPANA',
    OFFER_ID: 'OFFERID'
  },
  TICKET: {
    COMMUNICATION: {
      EMAIL: 'EMAIL'
    }
  },
  PARAMETER_TYPE: {
    BOOLEAN: {
      Inactivo: false,
      Activo: true
    }
  },
  FUNPACK: {
    FACEBOOK_PLAN_PRICE: 59.90
  },
  APPS_ILIMITADAS: 'Apps Ilimitadas',
  APPS_ILIMITADOS: 'Apps Ilimitados',
  FAMILY_PLAN: {
    PLAN_PARENT_CATALOG_ITEM_NAME: 'Plan',
    PLAN_OFFERING_ID: '3232618'
  },
  SUBSCRIBER_PLAN: {
    PLAN1: 'Llamadas Internacionales',
    PLAN2: 'Amigos y Familia (Dáos)',
    PLAN3: 'Limite de Consumo Adicional'
  },
  DATA_SHARE_CHILD_MEMBER_COUNT: 'implAffDeAffCount',
  DATA_SHARE_MULTIUSER_BO: '4364918',
  GTM_CONFIG: {
    TEST_DRIVE: {
      LAUNCH_CAMPAIGN: 'LAUNCH_CAMPAIGN',
      CLOSE_CAMPAIGN: 'CLOSE_CAMPAIGN',
      ACCEPT_CAMPAIGN: 'ACCEPT_CAMPAIGN',
      CANCEL_CAMPAIGN: 'CANCEL_CAMPAIGN',
      LAUNCH_CONFIRMATION: 'LAUNCH_CONFIRMATION',
      ACCEPT_CONFIRMATION: 'ACCEPT_CONFIRMATION',
      CANCEL_CONFIRMATION: 'CANCEL_CONFIRMATION',
      LAUNCH_SUCCESS: 'LAUNCH_SUCCESS',
      ACCEPT_SUCCESS: 'ACCEPT_SUCCESS'
    }
  },
  CARD_BRAND: {
    MASTERCARD: 'mastercard',
    DINER: 'diners',
    VISA: 'visa',
    AMEX: 'amex'
  },
  PREPLAN_FLEX: {
    BILLING_OFFER_ID: '4394703'
  },
  MT_LINES: {
    PRODUCT_OFFER_ID: '4269648'
  },
  PLAN_DURATION: {
    PLAN_DAYS_DURATION: 'Plan Days Duration'
  },
  PLAN_NAME: {
    BASIC_PREPAID: 'Prepago con Tarifa Única'
  },
  SEND_EMAIL_TEMPLATE: {
    BASE_TEMPLATE_ID: '83384',
    CHANGE_PLAN_TEMPLATE_ID: '168952',
    RECHARGE_TEMPLATE_ID: '149836',
    PAYMENT_TEMPLATE_ID: '150053'
  },
  CHANGE_PLAN_BLOCK_MEC_MSG: {
    API_MSG: 'Cambio de plan no está permitido cuando hay pendiente de Plan de cambio.',
    NEW_MSG: 'Ya tienes un Cambio de plan en proceso que se activará el '
  },
  CAPL_CONTRACT_LINK: 'DOC008',
  APP_DETAILS: {
    APP_ENVIRONMENT: 'DEVELOPMENT',
    APP_VERSION: '1.0.8'
  }

});
