# Digital Marketplace Frontend Jinja

Records breaking changes from major version bumps.

## Unreleased

## 3.7.1

Upgrade Digital Marketplace Frontend to v2.8.2

## 3.7.0

Upgrade Digital Marketplace Frontend to v2.8.1

## 3.6.0

Upgrade Digital Marketplace Frontend to v2.7.0

## 3.5.0

Upgrade Digital Marketplace Frontend to v2.6.0

## 3.4.0

Upgrade Digital Marketplace Frontend to v2.4.0

## 3.3.2

Fix issue with column width in list multiquestion

## 3.3.1

Upgrade Digital Marketplace Frontend to v2.3.1

## 3.3.0

Upgrade Digital Marketplace Frontend to v2.3.0

## 3.2.0

Upgrade Digital Marketplace Frontend to v2.2.0

## 3.1.0

Upgrade Digital Marketplace Frontend to v2.1.1

## 3.0.2

Make Python 3.11 the minimum supported version
Update the `pyproject.toml` to add dev dependancies

## 3.0.1

Upgrade Digital Marketplace Frontend to v2.0.2

## 3.0.0

Upgrade Digital Marketplace Frontend to v2.0.0

🆕 New features:

  Add macros for the following components:

  | Component name                      | Macro name                                          |
  |-------------------------------------|-----------------------------------------------------|
  | Question list multiquestion         | `digitalmarketplaceQuestionListMultiquestion`       |
  | Summary content text                | `digitalmarketplaceSummaryContentText`              |
  | Summary content list                | `digitalmarketplaceSummaryContentList`              |
  | Summary content upload              | `digitalmarketplaceSummaryContentUpload`            |
  | Summary content service ID          | `digitalmarketplaceSummaryContentServiceId`         |
  | Summary content radios              | `digitalmarketplaceSummaryContentRadios`            |
  | Summary content boolean             | `digitalmarketplaceSummaryContentBoolean`           |
  | Summary content number              | `digitalmarketplaceSummaryContentNumber`            |
  | Summary content checkbox tree       | `digitalmarketplaceSummaryContentCheckboxTree`      |
  | Summary content multiquestion       | `digitalmarketplaceSummaryContentMultiquestion`     |
  | Summary content list multiquestion  | `digitalmarketplaceSummaryContentListMultiquestion` |

## 2.11.0

Replace `setup.py` with `pyproject.toml`

## 2.10.0

Upgrade Digital Marketplace Frontend to v1.3.1

Update CCS GOV.UK Frontend Jinja to v1.3.0 (GOV.UK Frontend 5.7.1)

🆕 New features:

  Add macros for the following components:

  | Component name  | Macro name                          |
  |-----------------|-------------------------------------|
  | Question select | `digitalmarketplaceQuestionSelect`  |


## 2.9.0

Upgrade Digital Marketplace Frontend to v1.2.0

Update CCS GOV.UK Frontend Jinja to v1.2.1 (GOV.UK Frontend 5.4.1)


## 2.8.0

Update ccs-digitalmarketplace-utils to v67 which, in turn, updates flask to v3.0

Upgrade Digital Marketplace Frontend to v1.1


## 2.7.0

Make updates for change from Digital Marketplace GOV.UK Frontend to Digital Marketplace Frontend

Update CCS GOV.UK Frontend Jinja to v1.2 (GOV.UK Frontend 5.4.0)


## 2.6.0

Upgrade Digital Marketplace GOV.UK Frontend to v6.4


## 2.5.0

🆕 New features:

  Add macros for the following components:

  | Component name        | Macro name                              |
  |-----------------------|-----------------------------------------|
  | System message banner | `digitalmarketplaceSystemMessageBanner` |

  Remove macros for the following components:

  | Component name        | Macro name                              |
  |-----------------------|-----------------------------------------|
  | New framework banner  | `digitalmarketplaceNewFrameworkBanner`  |


## 2.4.0

Remove support for Python 3.9

Update flask support to v2.3


## 2.3.0

Add support for Python 3.12


## 2.2.0

Upgrade Digital Marketplace GOV.UK Frontend to v6.2


## 2.1.0

Use CCS GOV.UK Frontend Jinja to v1.0 (GOV.UK Frontend 5.3.1)


## 2.0.0

Upgrade GOV.UK Frontend Jinja to v3.0 (GOV.UK Frontend 5.1)


## 1.4.0

🆕 New features:

  Add macros for the following components:

  | Component name                          | Macro name                                                |
  |-----------------------------------------|-----------------------------------------------------------|
  | Compliance communication attachment row | `digitalmarketplaceComplianceCommunicationAttachmentRow`  |
  | Compliance communication attachments    | `digitalmarketplaceComplianceCommunicationAttachments`    |


## 1.2.0

Allow for use with all currently maintained Python versions:
- 3.9
- 3.10
- 3.11

Note, because ccs-digitalmarketplace-utils does not support 3.12 yet, neither can we.

## 1.1.0

Upgrade Flask to v2 and, therefore, Jinja to v3

Upgrade GOV.UK Frontend Jinja to v2.8 (GOV.UK Frontend 4.8)

## 1.0.0

🆕 New features:

  Add macros for the following components:

  | Component name            | Macro name                                  |
  |---------------------------|---------------------------------------------|
  | Alert                     | `digitalmarketplaceAlert`                   |
  | Attachment                | `digitalmarketplaceAttachment`              |
  | Banner                    | `digitalmarketplaceBanner`                  |
  | Character Count From Form | `digitalmarketplaceCharacterCountFromForm`  |
  | Checkboxes From Form      | `digitalmarketplaceCheckboxesFromForm`      |
  | Cookie Banner             | `digitalmarketplaceCookieBanner`            |
  | Documents                 | `digitalmarketplaceDocuments`               |
  | Footer                    | `digitalmarketplaceFooter`                  |
  | Header                    | `digitalmarketplaceHeader`                  |
  | Input From Form           | `digitalmarketplaceInputFromForm`           |
  | List Input                | `digitalmarketplaceListInput`               |
  | New Framework Banner      | `digitalmarketplaceNewFrameworkBanner`      |
  | Option Select             | `digitalmarketplaceOptionSelect`            |
  | Previous Next Pagination  | `digitalmarketplacePreviousNextPagination`  |
  | Question                  | `digitalmarketplaceQuestion`                |
  | Radios From Form          | `digitalmarketplaceRadiosFromForm`          |
  | Search Box                | `digitalmarketplaceSearchBox`               |
  | Select Country From Form  | `digitalmarketplaceSelectCountryFromForm`   |
  | Summary Content           | `digitalmarketplaceSummaryContent`          |
  | Temporary Message         | `digitalmarketplaceTemporaryMessage`        |

  Add the following layouts:

  - `layouts/_custom_dimensions.html`
  - `layouts/_site_verification.html`

  Add the following error page templates:

  - `errors/400.html`
  - `errors/403.html`
  - `errors/404.html`
  - `errors/410.html`
  - `errors/500.html`
