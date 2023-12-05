# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

import base64
import json
import jwt
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.x509 import load_pem_x509_certificate
from knack.cli import CLIError

from azext_attestation.generated._client_factory import cf_attestation_provider
from azext_attestation.vendored_sdks.azure_attestation.models._attestation_client_enums import TeeKind
from azext_attestation.vendored_sdks.azure_attestation.models._models_py3 import \
    AttestOpenEnclaveRequest, RuntimeData, InitTimeData
from azext_attestation.vendored_sdks.azure_mgmt_attestation.models import JsonWebKey
from azext_attestation.aaz.latest.attestation import Create as _AttestationCreate, Update as _AttestationUpdate,\
    Delete as _AttestationDelete, Show as _AttestationShow, GetDefaultByLocation as _AttestationGetDefaultByLocation
from azext_attestation.aaz.latest.attestation.policy import Reset as _ResetPolicy, Set as _SetPolicy, Show as _GetPolicy
from azext_attestation.aaz.latest.attestation.signer import Add as _AddSigner, Remove as _RemoveSigner,\
    List as _ListSigners
from azure.cli.core.aaz import has_value

tee_mapping = {
    TeeKind.tpm: 'TPM',
    TeeKind.sgx_intel_sdk: 'SgxEnclave',
    TeeKind.sgx_open_enclave_sdk: 'OpenEnclave'
}


def attestation_attestation_provider_show(client,
                                          resource_group_name=None,
                                          provider_name=None):
    """ Show the status of Attestation Provider. """
    return client.get(resource_group_name=resource_group_name,
                      provider_name=provider_name)


class AttestationShow(_AttestationShow):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZStrArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.id = AAZStrArg(
            options=["--id"],
            help="Resource ID of the provider. Please omit --resource-group/-g or --name/-n if you have already specified --id.",
        )
        args_schema.name = AAZStrArg(
            options=["--name", "-n"],
            help="Name of the attestation service instance.",
        )

        args_schema.provider_name._required = False
        args_schema.resource_group._required = False
        args_schema.provider_name._registered = False
        return args_schema

    def pre_operations(self):
        validate_provider_resource_id(self)


def _b64url_to_b64(s):
    return s.replace('-', '+').replace('_', '/') + ('=' * (4 - len(s) % 4) if len(s) % 4 else '')


def _b64_to_b64url(s):
    return s.rstrip('=').replace('+', '-').replace('/', '_')


def _b64_padding(s):
    return s + ('=' * (4 - len(s) % 4) if len(s) % 4 else '')


def attestation_attestation_provider_create(client,
                                            resource_group_name,
                                            provider_name,
                                            location,
                                            tags=None,
                                            certs_input_path=None):

    certs = []
    if not certs_input_path:
        certs_input_path = []

    for p in certs_input_path:
        expand_path = os.path.expanduser(p)
        if not os.path.exists(expand_path):
            raise CLIError('Path "{}" does not exist.'.format(expand_path))
        if not os.path.isfile(expand_path):
            raise CLIError('"{}" is not a valid file path.'.format(expand_path))

        with open(expand_path, 'rb') as f:
            pem_data = f.read()

        cert = load_pem_x509_certificate(pem_data, backend=default_backend())
        key = cert.public_key()
        if isinstance(key, rsa.RSAPublicKey):
            kty = 'RSA'
            alg = 'RS256'
        else:
            raise CLIError('Unsupported key type: {}'.format(type(key)))

        jwk = JsonWebKey(kty=kty, alg=alg, use='sig')
        jwk.x5c = [base64.b64encode(cert.public_bytes(Encoding.DER)).decode('ascii')]
        certs.append(jwk)

    return client.create(resource_group_name=resource_group_name,
                         provider_name=provider_name,
                         location=location,
                         tags=tags,
                         certs=certs)


class AttestationCreate(_AttestationCreate):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZStrArg, AAZListArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.id = AAZStrArg(
            options=["--id"],
            help="Resource ID of the provider. Please omit --resource-group/-g or --name/-n if you have already specified --id.",
        )
        args_schema.name = AAZStrArg(
            options=["--name", "-n"],
            help="Name of the attestation provider.",
        )
        args_schema.certs_input_path = AAZListArg(
            options=["--certs-input-path"],
            help="Space-separated file paths to PEM/DER files containing certificates.",
        )
        args_schema.certs_input_path.Element = AAZStrArg()
        args_schema.provider_name._required = False
        args_schema.resource_group._required = False
        args_schema.certs._registered = False
        args_schema.provider_name._registered = False
        return args_schema

    def pre_operations(self):
        args = self.ctx.args
        validate_provider_resource_id(self)
        certs = []
        if not has_value(args.certs_input_path):
            certs_input_path = []
        else:
            certs_input_path = args.certs_input_path.to_serialized_data()

        for p in certs_input_path:
            expand_path = os.path.expanduser(p)
            if not os.path.exists(expand_path):
                raise CLIError('Path "{}" does not exist.'.format(expand_path))
            if not os.path.isfile(expand_path):
                raise CLIError('"{}" is not a valid file path.'.format(expand_path))

            with open(expand_path, 'rb') as f:
                pem_data = f.read()

            cert = load_pem_x509_certificate(pem_data, backend=default_backend())
            key = cert.public_key()
            if isinstance(key, rsa.RSAPublicKey):
                kty = 'RSA'
                alg = 'RS256'
            else:
                raise CLIError('Unsupported key type: {}'.format(type(key)))

            jwk = {'kty': kty, 'alg': alg, 'use': 'sig',
                   'x5c': [base64.b64encode(cert.public_bytes(Encoding.DER)).decode('ascii')]}
            certs.append(jwk)
        args.certs = certs


def attestation_attestation_provider_delete(client,
                                            resource_group_name=None,
                                            provider_name=None):
    return client.delete(resource_group_name=resource_group_name,
                         provider_name=provider_name)


class AttestationDelete(_AttestationDelete):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZStrArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.id = AAZStrArg(
            options=["--id"],
            help="Resource ID of the provider. Please omit --resource-group/-g or --name/-n if you have already specified --id.",
        )
        args_schema.name = AAZStrArg(
            options=["--name", "-n"],
            help="Name of the attestation service instance.",
        )

        args_schema.provider_name._required = False
        args_schema.resource_group._required = False
        args_schema.provider_name._registered = False
        return args_schema

    def pre_operations(self):
        validate_provider_resource_id(self)


# class AttestationUpdate(_AttestationUpdate):
#     @classmethod
#     def _build_arguments_schema(cls, *args, **kwargs):
#         from azure.cli.core.aaz import AAZStrArg
#         args_schema = super()._build_arguments_schema(*args, **kwargs)
#         args_schema.name = AAZStrArg(
#             options=["--name", "-n"],
#             help="Name of the attestation provider.",
#         )
#
#         args_schema.provider_name._required = False
#         args_schema.resource_group._required = False
#         args_schema.provider_name._registered = False
#         return args_schema
#
#     def pre_operations(self):
#         validate_provider_resource_id(self)


def add_signer(cmd, client, signer=None, signer_file=None, resource_group_name=None, provider_name=None):
    if not signer and not signer_file:
        raise CLIError('Please specify one of parameters: --signer or --signer-file/-f')

    if signer and signer_file:
        raise CLIError('--signer and --signer-file/-f are mutually exclusive.')

    if signer_file:
        signer_file = os.path.expanduser(signer_file)
        if not os.path.exists(signer_file):
            raise CLIError('Signer file "{}" does not exist.'.format(signer_file))
        if not os.path.isfile(signer_file):
            raise CLIError('Signer file "{}" is not a valid file name.'.format(signer_file))
        with open(signer_file) as f:
            signer = f.read()

    provider_client = cf_attestation_provider(cmd.cli_ctx)
    provider = provider_client.get(resource_group_name=resource_group_name, provider_name=provider_name)
    token = client.add(tenant_base_url=provider.attest_uri, policy_certificate_to_add=signer)
    token = token.split(" ")[1].replace("}", "").strip("'")
    result = {'Jwt': token}

    if token:
        header = jwt.get_unverified_header(token)
        result.update({
            'Algorithm': header.get('alg', ''),
            'JKU': header.get('jku', '')
        })
        body = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False})
        result['Certificates'] = body.get('aas-policyCertificates', {}).get('keys', [])
        result['CertificateCount'] = len(result['Certificates'])

    return result


class AddSigner(_AddSigner):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZStrArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.signer_file = AAZStrArg(
            options=["--signer-file", "-f"],
            help="File name of the signer. (--signer and --signer-file/-f are mutually exclusive.).",
        )
        args_schema.id = AAZStrArg(
            options=["--id"],
            help="Resource ID of the provider. Please omit --resource-group/-g or --name/-n if you have already specified --id.",
        )
        args_schema.name = AAZStrArg(
            options=["--name", "-n"],
            help="Name of the attestation provider.",
        )

        args_schema.signer._required = False
        args_schema.provider_name._required = False
        args_schema.resource_group._required = False
        args_schema.provider_name._registered = False
        return args_schema

    def pre_operations(self):
        args = self.ctx.args
        validate_provider_resource_id(self)
        if not has_value(args.signer) and not has_value(args.signer_file):
            raise CLIError('Please specify one of parameters: --signer or --signer-file/-f')
        if has_value(args.signer) and has_value(args.signer_file):
            raise CLIError('--signer and --signer-file/-f are mutually exclusive.')
        signer = None
        if has_value(args.signer_file):
            signer_file = os.path.expanduser(args.signer_file.to_serialized_data())
            if not os.path.exists(signer_file):
                raise CLIError('Signer file "{}" does not exist.'.format(signer_file))
            if not os.path.isfile(signer_file):
                raise CLIError('Signer file "{}" is not a valid file name.'.format(signer_file))
            with open(signer_file) as f:
                signer = f.read()

        if signer:
            if type(signer) == bytes:
                args.signer = str(signer, encoding="utf-8")
            else:
                args.signer = signer

    def _output(self, *args, **kwargs):
        token = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)['token']
        result = {'Jwt': token}
        if has_value(token):
            header = jwt.get_unverified_header(token)
            result.update({
                'Algorithm': header.get('alg', ''),
                'JKU': header.get('jku', '')
            })
            body = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False})
            result['Certificates'] = body.get('aas-policyCertificates', {}).get('keys', [])
            result['CertificateCount'] = len(result['Certificates'])
        return result


def remove_signer(cmd, client, signer=None, signer_file=None, resource_group_name=None, provider_name=None):
    if not signer and not signer_file:
        raise CLIError('Please specify one of parameters: --signer or --signer-file/-f')

    if signer and signer_file:
        raise CLIError('--signer and --signer-file/-f are mutually exclusive.')

    if signer_file:
        signer_file = os.path.expanduser(signer_file)
        if not os.path.exists(signer_file):
            raise CLIError('Signer file "{}" does not exist.'.format(signer_file))
        if not os.path.isfile(signer_file):
            raise CLIError('Signer file "{}" is not a valid file name.'.format(signer_file))
        with open(signer_file) as f:
            signer = f.read()

    provider_client = cf_attestation_provider(cmd.cli_ctx)
    provider = provider_client.get(resource_group_name=resource_group_name, provider_name=provider_name)
    client.remove(tenant_base_url=provider.attest_uri, policy_certificate_to_remove=signer)
    return list_signers(cmd, client, resource_group_name, provider_name)


class RemoveSigner(_RemoveSigner):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZStrArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.signer_file = AAZStrArg(
            options=["--signer-file", "-f"],
            help="File name of the signer. (--signer and --signer-file/-f are mutually exclusive.).",
        )
        args_schema.id = AAZStrArg(
            options=["--id"],
            help="Resource ID of the provider. Please omit --resource-group/-g or --name/-n if you have already specified --id.",
        )
        args_schema.name = AAZStrArg(
            options=["--name", "-n"],
            help="Name of the attestation provider.",
        )

        args_schema.signer._required = False
        args_schema.provider_name._required = False
        args_schema.resource_group._required = False
        args_schema.provider_name._registered = False
        return args_schema

    def pre_operations(self):
        args = self.ctx.args
        validate_provider_resource_id(self)
        if not has_value(args.signer) and not has_value(args.signer_file):
            raise CLIError('Please specify one of parameters: --signer or --signer-file/-f')
        if has_value(args.signer) and has_value(args.signer_file):
            raise CLIError('--signer and --signer-file/-f are mutually exclusive.')
        signer = None
        if has_value(args.signer_file):
            signer_file = os.path.expanduser(args.signer_file.to_serialized_data())
            if not os.path.exists(signer_file):
                raise CLIError('Signer file "{}" does not exist.'.format(signer_file))
            if not os.path.isfile(signer_file):
                raise CLIError('Signer file "{}" is not a valid file name.'.format(signer_file))
            with open(signer_file) as f:
                signer = f.read()

        if signer:
            if type(signer) == bytes:
                args.signer = str(signer, encoding="utf-8")
            else:
                args.signer = signer

    def _output(self, *args, **kwargs):
        args = self.ctx.args
        list_args = {"resource_group": args.resource_group, "provider_name": args.provider_name}
        from azext_attestation.aaz.latest.attestation.signer import List
        token = List(cli_ctx=self.cli_ctx)(command_args=list_args)['token']
        result = {'Jwt': token}
        if has_value(token):
            header = jwt.get_unverified_header(token)
            result.update({
                'Algorithm': header.get('alg', ''),
                'JKU': header.get('jku', '')
            })
            body = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False})
            result['Certificates'] = body.get('x-ms-policy-certificates', {}).get('keys', [])
            result['CertificateCount'] = len(result['Certificates'])

        return result


def list_signers(cmd, client, resource_group_name=None, provider_name=None):
    provider_client = cf_attestation_provider(cmd.cli_ctx)
    provider = provider_client.get(resource_group_name=resource_group_name, provider_name=provider_name)
    signers = client.get(tenant_base_url=provider.attest_uri)
    token = json.loads(signers.replace('\'', '"')).get('token')
    result = {'Jwt': token}

    if token:
        header = jwt.get_unverified_header(token)
        result.update({
            'Algorithm': header.get('alg', ''),
            'JKU': header.get('jku', '')
        })
        body = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False})
        result['Certificates'] = body.get('x-ms-policy-certificates', {}).get('keys', [])
        result['CertificateCount'] = len(result['Certificates'])

    return result


class ListSigners(_ListSigners):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZStrArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.id = AAZStrArg(
            options=["--id"],
            help="Resource ID of the provider. Please omit --resource-group/-g or --name/-n if you have already specified --id.",
        )
        args_schema.name = AAZStrArg(
            options=["--name", "-n"],
            help="Name of the attestation provider.",
        )

        args_schema.provider_name._required = False
        args_schema.resource_group._required = False
        args_schema.provider_name._registered = False
        return args_schema

    def pre_operations(self):
        validate_provider_resource_id(self)

    def _output(self, *args, **kwargs):
        token = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)['token']
        result = {'Jwt': token}

        if has_value(token):
            header = jwt.get_unverified_header(token)
            result.update({
                'Algorithm': header.get('alg', ''),
                'JKU': header.get('jku', '')
            })
            body = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False})
            result['Certificates'] = body.get('x-ms-policy-certificates', {}).get('keys', [])
            result['CertificateCount'] = len(result['Certificates'])

        return result


def get_policy(cmd, client, attestation_type, resource_group_name=None, provider_name=None):
    """ Retrieves the current policy for a given kind of attestation type. """

    provider_client = cf_attestation_provider(cmd.cli_ctx)
    provider = provider_client.get(resource_group_name=resource_group_name, provider_name=provider_name)
    token = client.get(tenant_base_url=provider.attest_uri, tee=tee_mapping[attestation_type]).token
    result = {}

    if token:
        import jwt
        policy = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False}).get('x-ms-policy', '')
        result['Jwt'] = policy
        result['JwtLength'] = len(policy)
        result['Algorithm'] = None

        if policy:
            try:
                decoded_policy = jwt.decode(policy, algorithms=['RS256'], options={"verify_signature": False})
                decoded_policy = decoded_policy.get('AttestationPolicy', '')
                try:
                    new_decoded_policy = base64.b64decode(_b64url_to_b64(decoded_policy)).decode('ascii')
                    decoded_policy = new_decoded_policy
                except:  # pylint: disable=bare-except
                    pass
                finally:
                    result['Text'] = decoded_policy
                    result['TextLength'] = len(decoded_policy)
                    result['Algorithm'] = jwt.get_unverified_header(policy).get('alg', None)
            except:  # pylint: disable=bare-except
                result['Text'] = ''
                result['TextLength'] = 0

    return result


class GetPolicy(_GetPolicy):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZStrArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.id = AAZStrArg(
            options=["--id"],
            help="Resource ID of the provider. Please omit --resource-group/-g or --name/-n if you have already specified --id.",
        )
        args_schema.name = AAZStrArg(
            options=["--name", "-n"],
            help="Name of the attestation provider.",
        )

        args_schema.provider_name._required = False
        args_schema.resource_group._required = False
        args_schema.provider_name._registered = False
        return args_schema

    def pre_operations(self):
        validate_provider_resource_id(self)

    def _output(self, *args, **kwargs):
        token = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)['token']
        return handle_policy_output(token)


def handle_policy_output(token):
    result = {}

    if has_value(token):
        import jwt
        policy = jwt.decode(token, algorithms=['RS256'], options={"verify_signature": False}).get('x-ms-policy', '')
        result['Jwt'] = policy
        result['JwtLength'] = len(policy)
        result['Algorithm'] = None

        if has_value(policy):
            try:
                decoded_policy = jwt.decode(policy, algorithms=['RS256'], options={"verify_signature": False})
                decoded_policy = decoded_policy.get('AttestationPolicy', '')
                try:
                    new_decoded_policy = base64.b64decode(_b64url_to_b64(decoded_policy)).decode('ascii')
                    decoded_policy = new_decoded_policy
                except:  # pylint: disable=bare-except
                    pass
                finally:
                    result['Text'] = decoded_policy
                    result['TextLength'] = len(decoded_policy)
                    result['Algorithm'] = jwt.get_unverified_header(policy).get('alg', None)
            except:  # pylint: disable=bare-except
                result['Text'] = ''
                result['TextLength'] = 0
    return result


def set_policy(cmd, client, attestation_type, new_attestation_policy=None, new_attestation_policy_file=None,
               policy_format='Text', resource_group_name=None,
               provider_name=None):

    if new_attestation_policy_file and new_attestation_policy:
        raise CLIError('Please specify just one of --new-attestation-policy and --new-attestation-policy-file/-f')

    if not new_attestation_policy_file and not new_attestation_policy:
        raise CLIError('Please specify --new-attestation-policy or --new-attestation-policy-file/-f')

    if new_attestation_policy_file:
        file_path = os.path.expanduser(new_attestation_policy_file)
        if not os.path.exists(file_path):
            raise CLIError('Policy file "{}" does not exist.'.format(file_path))

        if not os.path.isfile(file_path):
            raise CLIError('"{}" is not a valid file name.'.format(file_path))

        with open(file_path) as f:
            new_attestation_policy = f.read()

    provider_client = cf_attestation_provider(cmd.cli_ctx)
    provider = provider_client.get(resource_group_name=resource_group_name, provider_name=provider_name)

    if policy_format == 'Text':
        if provider.trust_model != 'AAD':
            raise CLIError('Only supports Text policy under AAD model. Current model: {}. '
                           'If you are using signed JWT policy, please specify --policy-format JWT'.
                           format(provider.trust_model))

        import jwt
        try:
            new_attestation_policy = \
                base64.urlsafe_b64encode(new_attestation_policy.encode('ascii')).decode('ascii').strip('=')
            new_attestation_policy = {'AttestationPolicy': new_attestation_policy}
            new_attestation_policy = jwt.encode(
                new_attestation_policy, key='', algorithm='none'
            )
        except TypeError as e:
            print(e)
            raise CLIError('Failed to encode text content, are you using JWT? If yes, please use --policy-format JWT')

    client.set(
        tenant_base_url=provider.attest_uri,
        tee=tee_mapping[attestation_type],
        new_attestation_policy=new_attestation_policy
    )
    return get_policy(cmd, client, attestation_type,
                      resource_group_name=resource_group_name, provider_name=provider_name)


class SetPolicy(_SetPolicy):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZStrArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.new_attestation_policy_file = AAZStrArg(
            options=["--new-attestation-policy-file", "-f"],
            help="File name of the new attestation policy.",
        )
        args_schema.policy_format = AAZStrArg(
            options=["--policy-format"],
            default="Text",
            help="Specifies the format for the policy, either Text or JWT (JSON Web Token).  Allowed values: JWT, Text.",
        )
        args_schema.id = AAZStrArg(
            options=["--id"],
            help="Resource ID of the provider. Please omit --resource-group/-g or --name/-n if you have already specified --id.",
        )
        args_schema.name = AAZStrArg(
            options=["--name", "-n"],
            help="Name of the attestation provider.",
        )

        args_schema.new_attestation_policy._required = False
        args_schema.provider_name._required = False
        args_schema.resource_group._required = False
        args_schema.provider_name._registered = False
        return args_schema

    def pre_operations(self):
        args = self.ctx.args
        validate_provider_resource_id(self)

        if has_value(args.new_attestation_policy_file) and has_value(args.new_attestation_policy):
            raise CLIError('Please specify just one of --new-attestation-policy and --new-attestation-policy-file/-f')

        if not has_value(args.new_attestation_policy_file) and not has_value(args.new_attestation_policy):
            raise CLIError('Please specify --new-attestation-policy or --new-attestation-policy-file/-f')

        new_attestation_policy = None
        if has_value(args.new_attestation_policy_file):
            file_path = os.path.expanduser(args.new_attestation_policy_file.to_serialized_data())
            if not os.path.exists(file_path):
                raise CLIError('Policy file "{}" does not exist.'.format(file_path))

            if not os.path.isfile(file_path):
                raise CLIError('"{}" is not a valid file name.'.format(file_path))

            with open(file_path) as f:
                new_attestation_policy = f.read()

        provider_client = cf_attestation_provider(self.cli_ctx)
        provider = provider_client.get(resource_group_name=args.resource_group, provider_name=args.provider_name)

        if args.policy_format == 'Text':
            if provider.trust_model != 'AAD':
                raise CLIError('Only supports Text policy under AAD model. Current model: {}. '
                               'If you are using signed JWT policy, please specify --policy-format JWT'.
                               format(provider.trust_model))

            import jwt
            try:
                new_attestation_policy = \
                    base64.urlsafe_b64encode(new_attestation_policy.encode('ascii')).decode('ascii').strip('=')
                new_attestation_policy = {'AttestationPolicy': new_attestation_policy}
                new_attestation_policy = jwt.encode(
                    new_attestation_policy, key='', algorithm='none'
                )
            except TypeError as e:
                print(e)
                raise CLIError('Failed to encode text content, are you using JWT? If yes, please use --policy-format JWT')

        if new_attestation_policy:
            if type(new_attestation_policy) == bytes:
                args.new_attestation_policy = str(new_attestation_policy, encoding="utf-8")
            else:
                args.new_attestation_policy = new_attestation_policy

    def _output(self, *args, **kwargs):
        args = self.ctx.args
        show_args = {"resource_group": args.resource_group, "provider_name": args.provider_name, "attestation_type": args.attestation_type}
        from azext_attestation.aaz.latest.attestation.policy import Show
        token = Show(cli_ctx=self.cli_ctx)(command_args=show_args)['token']
        return handle_policy_output(token)


def validate_provider_resource_id(self):
    args = self.ctx.args
    if has_value(args.id):
        if has_value(args.resource_group) or has_value(args.name):
            raise CLIError('Please omit --resource-group/-g or --name/-n if you have already specified --id.')
        resource_id = args.id.to_serialized_data()
        args.resource_group = resource_id.split('/')[4]
        args.provider_name = resource_id.split('/')[8]
    elif not all([has_value(args.resource_group), has_value(args.name)]):
        raise CLIError('Please specify both --resource-group/-g and --name/-n.')

    if has_value(args.name):
        args.provider_name = args.name


def reset_policy(cmd, client, attestation_type, policy_jws='eyJhbGciOiJub25lIn0..', resource_group_name=None,
                 provider_name=None):

    provider_client = cf_attestation_provider(cmd.cli_ctx)
    provider = provider_client.get(resource_group_name=resource_group_name, provider_name=provider_name)
    client.reset(
        tenant_base_url=provider.attest_uri,
        tee=tee_mapping[attestation_type],
        policy_jws=policy_jws
    )
    return get_policy(cmd, client, attestation_type,
                      resource_group_name=resource_group_name, provider_name=provider_name)


class ResetPolicy(_ResetPolicy):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZStrArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.id = AAZStrArg(
            options=["--id"],
            help="Resource ID of the provider. Please omit --resource-group/-g or --name/-n if you have already specified --id.",
        )
        args_schema.name = AAZStrArg(
            options=["--name", "-n"],
            help="Name of the attestation provider.",
        )

        args_schema.provider_name._required = False
        args_schema.resource_group._required = False
        args_schema.policy_jws._required = False
        args_schema.provider_name._registered = False
        return args_schema

    def pre_operations(self):
        validate_provider_resource_id(self)

    def _output(self, *args, **kwargs):
        args = self.ctx.args
        show_args = {"resource_group": args.resource_group, "provider_name": args.provider_name, "attestation_type": args.attestation_type}
        from azext_attestation.aaz.latest.attestation.policy import Show
        token = Show(cli_ctx=self.cli_ctx)(command_args=show_args)['token']
        return handle_policy_output(token)


def attest_open_enclave(cmd, client, report=None, runtime_data=None, runtime_data_type=None, init_time_data=None,
                        init_time_data_type=None, resource_group_name=None, provider_name=None):

    provider_client = cf_attestation_provider(cmd.cli_ctx)
    provider = provider_client.get(resource_group_name=resource_group_name, provider_name=provider_name)

    request = AttestOpenEnclaveRequest(
        report=report,
        runtime_data=RuntimeData(
            data=runtime_data,
            data_type=runtime_data_type
        ),
        init_time_data=InitTimeData(
            data=init_time_data,
            data_type=init_time_data_type
        )
    )

    return client.attest_open_enclave(
        tenant_base_url=provider.attest_uri,
        request=request
    )


def attestation_attestation_provider_get_default_by_location(client,
                                                             loc):
    return client.get_default_by_location(location=loc)


class AttestationGetDefaultByLocation(_AttestationGetDefaultByLocation):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.location._fmt = None
        return args_schema
