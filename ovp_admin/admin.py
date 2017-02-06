from django.contrib import admin

import ovp_core.models as core
import ovp_users.models as user
import ovp_projects.models as project
import ovp_organizations.models as organization


adm_reg = admin.site._registry

if core.Lead in adm_reg:
	adm_reg[core.Lead].display_on_main_menu = True

if user.User in adm_reg:
	adm_reg[user.User].display_on_main_menu = True

if project.Project in adm_reg:
	adm_reg[project.Project].display_on_main_menu = True

if project.Apply in adm_reg:
	adm_reg[project.Apply].display_on_main_menu = True

if organization.Organization in adm_reg:
	adm_reg[organization.Organization].display_on_main_menu = True


try:
  import react_cms.models as react_cms
  if react_cms.ContentResource in adm_reg:
    adm_reg[react_cms.ContentResource].display_on_main_menu = True
except ImportError:
  pass