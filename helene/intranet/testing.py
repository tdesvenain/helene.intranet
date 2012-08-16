from plone.testing import z2

from plone.app.testing import *
import helene.intranet

FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                                zcml_package=helene.intranet,
                                additional_z2_products=[],
                                gs_profile_id='helene.intranet:default',
                                name="helene.intranet:FIXTURE")

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="helene.intranet:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="helene.intranet:Functional")

